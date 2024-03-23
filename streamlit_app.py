import streamlit as st
import openai

st.write('Welcome to Upload')

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

if __name__ == "__main__":
    main()
  
