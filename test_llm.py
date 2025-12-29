from openai import OpenAI

# Local Ollama server ki connect avthunnam
client = OpenAI(
    base_url='http://localhost:11434/v1',
    api_key='ollama', # Ollama ki real key akkarledhu, but placeholder thappadu
)
print("Script start ayyindi... AI ki message pamputhunnam...")
response = client.chat.completions.create(
  model="deepseek-r1:1.5b", # Nuvvu download chesina model name ikkada ivvu (e.g., llama3, mistral)
  messages=[
    {"role": "user", "content": "Tell me a short joke about engineers."}
  ]
)

print(response.choices[0].message.content)