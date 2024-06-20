import streamlit as st
from langchain_community.llms import Ollama
import pdfplumber  # for PDF files
import docx  # for DOCX files

# Initialize session state to keep track of the conversation
if 'user_input' not in st.session_state:
    st.session_state['user_input'] = []
if 'bot_response' not in st.session_state:
    st.session_state['bot_response'] = []

# Display chat messages function
def display_chat():
    for i, (user_input, bot_response) in enumerate(zip(st.session_state['user_input'], st.session_state['bot_response'])):
        if user_input:
            with st.chat_message("user", avatar="🕸️"):
                st.write(user_input)
        if bot_response:
            st.markdown(bot_response)

# Create a title
st.markdown("<h1 style='text-align: center; color: #c2c2ff; line-height: 0px;'>PAV AI</h1>", unsafe_allow_html=True)

# Add a top divider-1 with a specific height
st.markdown("<hr style='height:0px;'/>", unsafe_allow_html=True)

# Display chat messages at the top
display_chat()

# Add a bottom divider with a specific height
st.markdown("<hr style='height:300px;'/>", unsafe_allow_html=True)

# Select model
with st.sidebar:
    model = st.selectbox("Select a model:", ["phi3", "llama3", "mistral", "gemma"])
llm = Ollama(model=model)

# Upload file and ask question
uploaded_file = st.file_uploader("Upload a file (PDF, DOCX, TXT):", type=["pdf", "docx", "txt"])
if uploaded_file:
    if uploaded_file.type == "application/pdf":
        with pdfplumber.open(uploaded_file) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text()
    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        doc = docx.Document(uploaded_file)
        text = ""
        for para in doc.paragraphs:
            text += para.text
    else:
        text = uploaded_file.read().decode("utf-8")

    user_input = st.chat_input("Enter your question about the file:")

    if user_input:
        with st.spinner("Generating response..."):
            try:
                # Add a stop generation button
                stop_generation = st.button("Stop Generation")
                if stop_generation:
                    st.stop()
                bot_response = llm.stream(user_input + " " + text, stop=['\n'])
                bot_response = ''.join([i for i in bot_response])  # Convert generator to string
            except Exception as e:
                bot_response = f"Error: {e}"

            # Append the new user input and bot response to the session state
        st.session_state['user_input'].append(user_input)
        st.session_state['bot_response'].append(bot_response)

        # Rerun the script to update the chat display
        st.rerun()

else:
    user_input = st.chat_input("Ask....")
    if user_input:
        with st.spinner("Generating response..."):
            try:
                # Add a stop generation button
                stop_generation = st.button("Stop Generation")
                if stop_generation:
                    st.stop()
                bot_response = llm.invoke(user_input).strip()
            except Exception as e:
                bot_response = f"Error: {e}"

            # Append the new user input and bot response to the session state
        st.session_state['user_input'].append(user_input)
        st.session_state['bot_response'].append(bot_response)

        # Rerun the script to update the chat display
        st.rerun()
