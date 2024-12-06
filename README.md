# PDF to ChatGPT Summarizer

## Overview
**PDF to ChatGPT Summarizer** is a simple Python-based tool designed to streamline the process of extracting text from PDF documents, formatting the content, and preparing a prompt for ChatGPT to generate summaries. This way you can quickly work with o1 too, which does not accept file upload yet.

## Features
- **PDF Parsing:** Extracts text content from PDF files using `PyPDF2`.
- **Flexible Formatting:** Supports output in plain text (`txt`), Markdown (`md`), or HTML (`html`).
- **Context Window Handling:** Automatically splits large documents into manageable snippets based on a specified context window size.
- **Snippet Selection:** Allows processing of specific snippets within the document.
- **Custom Prompts:** Enables the use of custom prompts tailored to specific needs.
- **Clipboard Integration:** Automatically copies the prepared prompt to your system clipboard using `pyperclip`.
- **Seamless ChatGPT Integration:** Opens the ChatGPT web interface in your default browser for immediate interaction.
- **User-Friendly:** Command-line interface with clear instructions.

## Prerequisites
Before using the tool, ensure you have the following installed:
- **Python 3.7 or higher:** [Download Python](https://www.python.org/downloads/)
- **pip:** Python package installer (comes with Python)

## Installation
1. **Clone the Repository:**

   ```bash
   git clone https://github.com/CrispStrobe/pdf-gpt-summarizer.git
   ```

2. **Navigate to the Project Directory:**

   ```bash
   cd pdf-gpt-summarizer
   ```

3. **Create a Virtual Environment (Optional but Recommended):**

   ```bash
   python -m venv venv
   ```

4. **Activate the Virtual Environment:**

   - **Windows:**
     ```bash
     venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     source venv/bin/activate
     ```

5. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Usage
Run the script using Python with the required arguments.

### Basic Command Structure:

```bash
python copy-and-paste-pdf.py path/to/document.pdf --format [txt|md|html]
```

### Advanced Options:
- **`--context`**: Specify the maximum number of characters per prompt/snippet. Defaults to `128000`.

  ```bash
  --context 64000
  ```

- **`--snippet`**: Select a specific snippet to process. For example, `--snippet 2` processes the second snippet.

  ```bash
  --snippet 3
  ```

- **`--prompt`**: Use a custom prompt instead of the default instruction.

  ```bash
  --prompt "Make a joke of this:"
  ```

### Examples:
1. **Default Usage (TXT Format):**

   ```bash
   python copy-and-paste-pdf.py ./documents/sample.pdf
   ```

2. **Markdown Format with Default Context:**

   ```bash
   python copy-and-paste-pdf.py ./documents/sample.pdf --format md
   ```

3. **HTML Format with Custom Context Window:**

   ```bash
   python copy-and-paste-pdf.py ./documents/sample.pdf --format html --context 64000
   ```

4. **Process a Specific Snippet:**

   ```bash
   python copy-and-paste-pdf.py ./documents/sample.pdf --snippet 2
   ```

5. **Use a Custom Prompt:**

   ```bash
   python copy-and-paste-pdf.py ./documents/sample.pdf --prompt "Explain the following in simple terms:"
   ```

6. **Combine Multiple Options:**

   ```bash
   python copy-and-paste-pdf.py ./documents/large_document.pdf --context 64000 --snippet 3 --prompt "Analyze the following section:"
   ```

## Workflow
1. **Run the Script:**

   Execute the command with the appropriate arguments.

2. **Script Actions:**
   - Extracts text from the specified PDF.
   - Formats the content based on the chosen format.
   - If the content exceeds the specified context window, splits it into snippets.
   - Constructs prompts with or without framing based on the number of snippets.
   - Copies the selected prompt(s) to your clipboard.
   - Opens the ChatGPT web interface in your default browser.

3. **Finalize in ChatGPT:**
   - In the opened ChatGPT window, click on the input box.
   - Paste the prompt using `Ctrl+V` (Windows/Linux) or `Cmd+V` (Mac).
   - Press `Enter` to send the prompt for summarization.

## License
This project is licensed under the [MIT License](LICENSE).

## Acknowledgements
- [PyPDF2](https://pypi.org/project/PyPDF2/) for PDF parsing.
- [pyperclip](https://pyperclip.readthedocs.io/en/latest/) for clipboard operations.
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) for HTML formatting.
- [OpenAI](https://openai.com/) for ChatGPT integration.
