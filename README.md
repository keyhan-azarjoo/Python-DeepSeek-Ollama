# python-DeepSeek
DeepSeek in local


1. install ollama from : https://ollama.com/download
2. make sure ollama is in computer Path
3. open CMD:
	1. -ollama	
	2. -ollama pull deepseek-r1
	3. -ollama run deepseek-r1
	4. -cd c:\code\python\deepseek-r1
	5. -python -m venv env1
	6. -env1\Scripts\activate.bat
	7. -pip install ollama
	8. -pip install streamlit
	
	
To see the list of model pulled from ollama :
	-ollama list
	
	
in CMD:
	1. -code .
	
in vs code:
	1. Create a new file from file -> new file (test.py)

put this code there:

==========================================================================================================
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
==========================================================================================================

in CMD:
	- streamlit run deepseekr1-python.py
