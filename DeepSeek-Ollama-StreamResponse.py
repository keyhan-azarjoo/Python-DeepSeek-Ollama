# Stream

import streamlit as st
import ollama
import torch
import time

# Check if CUDA is available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

# Example tensor to be moved to GPU
tensor = torch.randn(10, 10).to(device)

desiredModel = 'deepseek-r1:latest'

st.title("LLM Model (DeepSeek-R1)")

def generate_response(questionToAsk):
    # Create a placeholder for streaming output
    placeholder = st.empty()
    
    displayed_text = ""  # Accumulate displayed text

    # Streaming response from Ollama
    for chunk in ollama.chat(model=desiredModel, messages=[
        {'role': 'user', 'content': questionToAsk}
    ], stream=True):  # Enable streaming
        if 'message' in chunk and 'content' in chunk['message']:
            for word in chunk['message']['content'].split():  # Split into words
                displayed_text += word + " "  # Append word
                placeholder.write(displayed_text)  # Update UI
                time.sleep(0.2)  # Simulate typing delay

with st.form("my_form"):
    text = st.text_area("Enter text:", "")
    submitted = st.form_submit_button("Submit")
    if submitted:
        generate_response(text)
