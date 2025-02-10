# python-DeepSeek
DeepSeek in local

https://www.youtube.com/watch?v=LMO9H0NVUv0


1. Install ollama from : https://ollama.com/download
2. Make sure ollama is in computer Path
3. Open CMD:
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
	
	
In CMD:
	1. -code .
	
In vs code:
	1. Create a new file from file -> new file (test.py)

Put this code in deepseekr1-python in your new python file 

In CMD:
	- streamlit run deepseekr1-python.py



To change download model path in environment :
VariableName : OLLAMA_MODELS
VariableValue : E:\OllamaModel\models      (download model path)
