from embedchain import App
from ollama_llm import OllamaLLm

app = App(llm=OllamaLLm())
response = app.query("How many companies does Elon Musk run and name those?")
print(response)