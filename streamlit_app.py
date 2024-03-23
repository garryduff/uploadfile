import streamlit as st
import openai

st.write('Welcome to Upload')
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Streamlit app
def main():
    st.title('File Processor with OpenAI')

    uploaded_file = st.file_uploader("Choose a file")

    if uploaded_file is not None:
        # Process the file
        result = process_file(uploaded_file)
        
        # Display the result
        st.write("Summary:")
        st.write(result)

def process_file(file):
    # Read the file content
    content = file.getvalue().decode("utf-8")
    
    # Use OpenAI API to process the content. For example, let's say we want to summarize the text.
    response = openai.Completion.create(
      engine="text-davinci-003",  # Choose an appropriate engine for your task
      prompt="Summarize this text: \n" + content,
      max_tokens=150  # Adjust based on how long you expect the response to be
    )
    
    return response.choices[0].text.strip()
    
if __name__ == "__main__":
    main()
  
