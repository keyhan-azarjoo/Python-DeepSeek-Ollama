import streamlit as st
import ollama
desiredModel = 'deepseek-r1:latest'

st.title("LLM Model(DeepSeek-R1)")

def generate_response(questionToAsk):

    response = ollama.chat(model= desiredModel, messages = [
        {
            'role' : 'user',
            'content' : questionToAsk,
        },
    ])

    st.info(response['message']['content'])


with st.form("my_form"):
    text = st.text_area(
        "Enter text:",
        "Over here, ask a question and press the submit button. ",
    )
    submitted = st.form_submit_button("Submit")
    if submitted:
        generate_response(text)