# PAV AI - Local AI Chat Web App

PAV AI is a Streamlit-based application that uses locally running LLMs (Large Language Models) to allow users to ask questions to AI models or upload files (PDF, DOCX, TXT) and inquire about their contents. It utilizes the `langchain_community.llms` library to generate responses based on the uploaded file content and the user's questions.

## Features

- Interactive chat interface
- Ask questions to AI models
- Upload PDF, DOCX, or TXT files
- Inquire about the content of uploaded files
- Select different language models to generate responses
- Operates offline once fully established
- Compatible with Windows and Linux

## Requirements

- Python 3.7 or higher
- Streamlit
- `langchain_community.llms`
- `pdfplumber`
- `python-docx`

## Installation

### Local LLM Using Ollama

1. Install Ollama from (https://www.ollama.com/).
2. Run the Ollama app, ensuring it is running on `http://localhost:11434` by using the command line:
    ```sh
    ollama serve
    ```
3. Pull the required models from the command line:
    ```sh
    ollama pull model_name
    ```
   For this app, we use `llama3`, `phi3`, and `mistral` models.

### App Installation

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

3. Ask questions to the model or upload a file (PDF, DOCX, or TXT) and enter your question to get a response.

## How It Works

- PAV AI is a chat application with locally running LLMs.
- Users can select a language model from the sidebar.
- Users can ask questions directly to the model or upload a file and ask questions about its content.
- The selected language model generates responses based on the user's input and the extracted text from the uploaded file.

## License

This project is licensed under the MIT License.
