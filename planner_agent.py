import subprocess

def query_fin_agent(prompt):
    full_prompt = f"You are a financial assistant. Answer this clearly: {prompt}"
    result = subprocess.run(["ollama", "run", "tinyllama", full_prompt], capture_output=True, text=True)
    return result.stdout.strip()
