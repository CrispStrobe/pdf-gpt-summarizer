
# PDF to ChatGPT Summarizer

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)
- [Contact](#contact)

## Overview

**PDF to ChatGPT Summarizer** is a Python-based tool designed to streamline the process of extracting text from PDF documents, formatting the content, and preparing a prompt for ChatGPT to generate summaries. This tool automates the workflow, making it easier to obtain concise summaries from lengthy PDF files.

## Features

- **PDF Parsing:** Extracts text content from PDF files using `PyPDF2`.
- **Flexible Formatting:** Supports output in plain text (`txt`), Markdown (`md`), or HTML (`html`).
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

   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux:
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
python pdf_to_chatgpt.py path/to/document.pdf --format [txt|md|html]
```

### Parameters:

- `path/to/document.pdf`: (Required) The path to the PDF file you want to summarize.
- `--format`: (Optional) The output format. Choose from `txt` (default), `md`, or `html`.

### Examples:

1. **Default Format (TXT):**

   ```bash
   python pdf_to_chatgpt.py ./documents/sample.pdf
   ```

2. **Markdown Format:**

   ```bash
   python pdf_to_chatgpt.py ./documents/sample.pdf --format md
   ```

3. **HTML Format:**

   ```bash
   python pdf_to_chatgpt.py ./documents/sample.pdf --format html
   ```

### Workflow:

1. **Run the Script:**

   Execute the command with the appropriate arguments.

2. **Script Actions:**

   - Extracts text from the specified PDF.
   - Formats the content based on the chosen format.
   - Constructs a prompt: "Summarize the following text into no longer than 800 words:"
   - Copies the prompt to your clipboard.
   - Opens the ChatGPT web interface in your default browser.

3. **Finalize in ChatGPT:**

   - In the opened ChatGPT window, click on the input box.
   - Paste the prompt using `Ctrl+V` (Windows/Linux) or `Cmd+V` (Mac).
   - Press Enter to send the prompt for summarization.

### Sample Command:

```bash
python pdf_to_chatgpt.py ./docs/report.pdf --format md
```

## Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the Repository**

2. **Create a Feature Branch**

   ```bash
   git checkout -b feature/YourFeatureName
   ```

3. **Commit Your Changes**

   ```bash
   git commit -m "Add Your Feature"
   ```

4. **Push to the Branch**

   ```bash
   git push origin feature/YourFeatureName
   ```

5. **Open a Pull Request**

Please ensure your contributions adhere to the following guidelines:

- Follow the existing code style.
- Write clear commit messages.
- Include relevant documentation or tests for new features.

## License

This project is licensed under the MIT License.

## Acknowledgements

- PyPDF2 for PDF parsing.
- pyperclip for clipboard operations.
- Beautiful Soup for HTML formatting.
- OpenAI for ChatGPT integration.

