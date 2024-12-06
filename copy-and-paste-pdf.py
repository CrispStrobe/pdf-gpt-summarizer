import argparse
import sys
import os
import webbrowser
import pyperclip
from PyPDF2 import PdfReader

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

def build_prompt(formatted_text):
    """
    Builds the prompt by concatenating the instruction with the formatted text.

    :param formatted_text: The formatted text to be summarized.
    :return: The complete prompt as a string.
    """
    prompt = "Summarize the following text into no longer than 800 words:\n\n" + formatted_text
    return prompt

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
    parser = argparse.ArgumentParser(description="PDF to ChatGPT Summarizer")
    parser.add_argument('pdf_path', help='Path to the PDF file to be summarized.')
    parser.add_argument('--format', choices=['txt', 'md', 'html'], default='txt',
                        help='Output format: txt (default), md, or html.')
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

    print("Building the prompt...")
    prompt = build_prompt(formatted_text)

    print("Copying the prompt to the clipboard...")
    copy_to_clipboard(prompt)

    print("Opening ChatGPT in your default browser...")
    open_chatgpt()

    print("\n=== Instructions ===")
    print("1. In the opened ChatGPT window, click on the input box.")
    print("2. Press Ctrl+V (Windows/Linux) or Cmd+V (Mac) to paste the prompt.")
    print("3. Press Enter to send the prompt to ChatGPT for summarization.")
    print("====================\n")

if __name__ == "__main__":
    main()

