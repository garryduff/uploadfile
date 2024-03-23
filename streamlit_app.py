import streamlit as st
import openai

# Set up Streamlit and OpenAI API key
st.write('Welcome to Upload')
openai.api_key = st.secrets["OPENAI_API_KEY"]

def main():
    st.title('File Processor with OpenAI')

    uploaded_file = st.file_uploader("Choose a file")

    if uploaded_file is not None:
        # Upload the file directly to OpenAI
        upload_to_openai(uploaded_file)

def upload_to_openai(file):
    # OpenAI expects the file to be in a binary format, so we use the 'rb' mode.
    # Streamlit's UploadedFile type supports this directly using the `.getvalue()` method.
    response = openai.File.create(
        file=file.getvalue(),
        purpose="fine-tune"
    )
    
    # Optionally, display a message or the response from OpenAI
    st.write("File uploaded to OpenAI successfully.")

if __name__ == "__main__":
    main()
