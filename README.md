# localAichatWEbaPP-PAVI-Ai
# PAV AI

PAV AI is a Streamlit-based application that allows users to upload files (PDF, DOCX, TXT) and ask questions about their contents. It uses the `langchain_community.llms` library to generate responses based on the uploaded file content and the user's question.

## Features

- Upload PDF, DOCX, or TXT files.
- Ask questions about the uploaded file.
- Select different language models to generate responses.
- Interactive chat interface with session state management.

## Requirements

- Python 3.7 or higher
- Streamlit
- langchain_community.llms
- pdfplumber
- python-docx

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/your-username/your-repository.git
    cd your-repository
    ```

2. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the Streamlit app:

    ```sh
    streamlit run app.py
    ```

2. Open your web browser and go to `http://localhost:8501` to access the app.

3. Upload a file (PDF, DOCX, or TXT) and enter your question to get a response.

## How It Works

- The app initializes session state variables to keep track of the conversation.
- Users can select a language model from the sidebar.
- Users can upload a file and ask questions about its content.
- The app uses `pdfplumber` for PDF files and `python-docx` for DOCX files to extract text.
- The selected language model generates responses based on the user's input and the extracted text from the uploaded file.

## License

This project is licensed under the MIT License.

