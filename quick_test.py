# quick_test.py
import requests
import time

print("Quick test with shorter prompt...")

prompt = "What is RAG? Answer in one sentence."

start = time.time()
print("Sending request to LM Studio...")

response = requests.post(
    "http://localhost:1234/v1/chat/completions",
    json={
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7,
        "max_tokens": 100  # Chhota response
    },
    timeout=60
)

end = time.time()

if response.status_code == 200:
    answer = response.json()["choices"][0]["message"]["content"]
    print(f"\n✅ Answer: {answer}")
    print(f"⏱️ Time taken: {end-start:.2f} seconds")
else:
    print(f"❌ Error: {response.status_code}")
    print(response.text)