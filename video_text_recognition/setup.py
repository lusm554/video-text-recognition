import subprocess

def step1_pip_install():
  subprocess.run("pip install -r requirements.txt")

def step2_download_ollama_linux():
  subprocess.run('curl -fsSL https://ollama.com/install.sh | sh')

def step3_run_ollama_serve():
  subprocess.run('ollama serve')

def step4_download_llama3():
  subprocess.run('ollama pull llama3:8b')

def step5_download_easyocr():
  from setup_environment import download_easyocr_model
  download_easyocr_model()


