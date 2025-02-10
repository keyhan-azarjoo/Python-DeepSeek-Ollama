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



## To change download model path in environment :

VariableName : OLLAMA_MODELS

VariableValue : E:\OllamaModel\models      (download model path)



### To Run On cuda :
## For CPU Only:
-pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
## For CUDA 12.1:
-pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
## For CUDA 11.8:
-pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118



### To Add Virtual memory 

To increase your virtual memory (pagefile) to 400 GB, follow these steps:

### Step 1: Check Available Disk Space
		You need at least 400 GB of free space on your storage drive (preferably an SSD for performance).
### Step 2: Open Virtual Memory Settings
		1. Press Win + R, type sysdm.cpl, and press Enter.
		2. Go to the Advanced tab.
		3. Under Performance, click Settings.
		4. Go to the Advanced tab in the new window.
		5. Under Virtual Memory, click Change.
### Step 3: Set Virtual Memory Size
		1. Uncheck "Automatically manage paging file size for all drives."
		2. Select your drive (e.g., C:).
		3. Click Custom size and enter:
		4. Initial size (MB): 409600 (400 GB)
		5. Maximum size (MB): 409600 (400 GB)
		6. Click Set and then OK.
### Step 4: Restart Your Computer
		1. Restart your PC to apply the new virtual memory settings.
### Performance Considerations
- SSD vs. HDD: Using an SSD for virtual memory is faster than an HDD.
- RAM vs. Pagefile: Virtual memory is not as fast as RAM, but it helps when you run out of physical RAM.
- Large Pagefile Impact: A massive pagefile (400 GB) will reduce available storage space and may cause excessive SSD wear if heavily used.
