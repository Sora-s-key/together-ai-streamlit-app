import streamlit as st
import os
from together import Together

# Get the API key from Streamlit secrets
api_key = st.secrets["TOGETHER_API_KEY"]

# Optionally set an environment variable if needed by Together
os.environ["TOGETHER_API_KEY"] = api_key

# Initialize Together client using the API key directly
client = Together(api_key=api_key)

def generate_code_with_codellama(description):
    """
    Generate Python code based on a natural language description using CodeLlama.
    """
    # Use the client and the description to generate code
    # (Fill in with the appropriate Together API call)
    response = client.run_code_model(
        model="codellama-34b",  # example model name
        prompt=description
    )
    return response
    
# Streamlit UI
st.title("Python Code Generator with CodeLlama")
user_input = st.text_input("Application or Code Description", "Write a Python script to reverse a string")
if st.button("Generate Code"):
    code = generate_code_with_codellama(user_input)
    st.markdown("### Generated Python Code")
    st.code(code, language="python")
