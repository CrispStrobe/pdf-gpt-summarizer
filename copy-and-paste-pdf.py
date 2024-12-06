import argparse
import sys
import os
import webbrowser
import pyperclip
from PyPDF2 import PdfReader
import re

def extract_text_from_pdf(pdf_path):
    """
    Extracts text from a PDF file using PyPDF2.

    :param pdf_path: Path to the PDF file.
    :return: Extracted text as a string.
    """
    try:
        reader = PdfReader(pdf_path)
        text = ""
        for page_num, page in enumerate(reader.pages, start=1):
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
            else:
                print(f"Warning: No text found on page {page_num}.")
        return text
    except Exception as e:
        print(f"Error reading PDF file: {e}")
        sys.exit(1)

def format_content(text, format_type):
    """
    Formats the extracted text based on the specified format.

    :param text: The extracted text.
    :param format_type: The desired format ('txt', 'md', 'html').
    :return: Formatted text as a string.
    """
    if format_type == 'txt':
        return text
    elif format_type == 'md':
        # Simple markdown formatting: paragraphs separated by blank lines
        paragraphs = text.split('\n\n')
        markdown = '\n\n'.join(paragraphs)
        return markdown
    elif format_type == 'html':
        # Simple HTML formatting: wrap paragraphs in <p> tags
        paragraphs = text.split('\n\n')
        html_paragraphs = ''.join([f'<p>{para.strip()}</p>' for para in paragraphs if para.strip()])
        return html_paragraphs
    else:
        print(f"Unsupported format: {format_type}")
        sys.exit(1)

def split_into_snippets(text, context_size):
    """
    Splits the text into snippets that fit within the specified context window size.

    :param text: The text to split.
    :param context_size: Maximum size of each snippet in characters.
    :return: List of text snippets.
    """
    # Split text into sentences using regex to ensure proper sentence boundaries
    sentences = re.split(r'(?<=[.!?]) +', text)
    
    snippets = []
    current_snippet = ""
    
    for sentence in sentences:
        # Check if adding the next sentence exceeds the context size
        if len(current_snippet) + len(sentence) + 1 > context_size:
            if current_snippet:
                snippets.append(current_snippet.strip())
                current_snippet = sentence + " "
            else:
                # Single sentence exceeds context size; force split
                snippets.append(sentence.strip())
                current_snippet = ""
        else:
            current_snippet += sentence + " "
    
    # Add any remaining text as the last snippet
    if current_snippet.strip():
        snippets.append(current_snippet.strip())
    
    return snippets

def build_snippet_frame(part_number, total_parts, snippet):
    """
    Frames the snippet with part notifications.

    :param part_number: The current part number.
    :param total_parts: The total number of parts.
    :param snippet: The text snippet.
    :return: Framed snippet as a string.
    """
    framed_snippet = f"---\nPart {part_number} of {total_parts}:\n\n{snippet}\n\nEnd of Part {part_number}.\n---"
    return framed_snippet

def copy_to_clipboard(text):
    """
    Copies the given text to the system clipboard.

    :param text: Text to copy.
    """
    try:
        pyperclip.copy(text)
        print("Prompt has been copied to the clipboard.")
    except Exception as e:
        print(f"Failed to copy to clipboard: {e}")
        sys.exit(1)

def open_chatgpt():
    """
    Opens the ChatGPT web interface in the default browser.
    """
    url = "https://chat.openai.com/chat"
    try:
        webbrowser.open(url)
        print(f"Opened {url} in your default browser.")
    except Exception as e:
        print(f"Failed to open browser: {e}")
        sys.exit(1)

def parse_arguments():
    """
    Parses command-line arguments.

    :return: Parsed arguments.
    """
    parser = argparse.ArgumentParser(description="PDF to ChatGPT Summarizer with Enhanced Features")
    parser.add_argument('pdf_path', help='Path to the PDF file to be summarized.')
    parser.add_argument('--format', choices=['txt', 'md', 'html'], default='txt',
                        help='Output format: txt (default), md, or html.')
    parser.add_argument('--context', type=int, default=128000,
                        help='Context window size in characters (default: 128000).')
    parser.add_argument('--snippet', type=int, default=None,
                        help='Specify which snippet to process (e.g., 3). If not set, all snippets will be processed.')
    parser.add_argument('--prompt', type=str, default=None,
                        help='Custom prompt to use instead of the default instruction.')
    return parser.parse_args()

def main():
    args = parse_arguments()

    if not os.path.isfile(args.pdf_path):
        print(f"Error: File '{args.pdf_path}' does not exist.")
        sys.exit(1)

    print(f"Extracting text from '{args.pdf_path}'...")
    extracted_text = extract_text_from_pdf(args.pdf_path)

    if not extracted_text.strip():
        print("Error: No text extracted from the PDF.")
        sys.exit(1)

    print(f"Formatting content as '{args.format}'...")
    formatted_text = format_content(extracted_text, args.format)

    context_size = args.context
    print(f"Using context window size: {context_size} characters.")

    # Check if content exceeds context window
    if len(formatted_text) > context_size:
        print("Content exceeds the context window. Splitting into snippets...")
        # Reserve space for framing notifications (approximate)
        reserved_space = 500
        snippets = split_into_snippets(formatted_text, context_size - reserved_space)
        total_snippets = len(snippets)
        print(f"Total snippets created: {total_snippets}")
    else:
        snippets = [formatted_text]
        total_snippets = 1
        print("Content fits within the context window.")

    # Determine which snippets to process
    if args.snippet:
        if args.snippet < 1 or args.snippet > total_snippets:
            print(f"Error: --snippet must be between 1 and {total_snippets}.")
            sys.exit(1)
        selected_snippets = [snippets[args.snippet - 1]]
        selected_total = total_snippets
        print(f"Processing snippet {args.snippet} of {total_snippets}.")
    else:
        selected_snippets = snippets
        selected_total = total_snippets
        if total_snippets > 1:
            print("Processing all snippets.")
        else:
            print("Processing the single snippet.")

    # Define the prompt instruction
    default_prompt = "Summarize the following text into no longer than 800 words:"
    prompt_instruction = args.prompt if args.prompt else default_prompt

    # Build the complete prompt
    complete_prompt = ""

    if selected_total > 1:
        # Add the prompt instruction once at the beginning
        complete_prompt += f"{prompt_instruction}\n\n"
        for idx, snippet in enumerate(selected_snippets, start=1):
            part_number = args.snippet if args.snippet else idx
            framed_snippet = build_snippet_frame(part_number, selected_total, snippet)
            complete_prompt += f"{framed_snippet}\n\n"
    else:
        # Single snippet without framing
        complete_prompt += f"{prompt_instruction}\n\n{selected_snippets[0]}"

    print("Copying the prompt to the clipboard...")
    copy_to_clipboard(complete_prompt.strip())

    print("Opening ChatGPT in your default browser...")
    open_chatgpt()

    print("\n=== Instructions ===")
    print("1. In the opened ChatGPT window, click on the input box.")
    print("2. Press Ctrl+V (Windows/Linux) or Cmd+V (Mac) to paste the prompt.")
    print("3. Press Enter to send the prompt to ChatGPT for summarization.")
    print("====================\n")

if __name__ == "__main__":
    main()
