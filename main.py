# main.py
from agents import planner, answer_agent, user_proxy, search_docs, count_words

print("="*50)
print("🎓 AGENTIC RESEARCH ASSISTANT")
print("="*50)

# User se question lo
question = input("\n💬 Ask a question: ").strip()

if not question:
    question = "Compare RAG and fine-tuning in LLMs with examples."
    print(f"\nUsing default: {question}")

print("\n" + "="*50)

# STEP 1: Search documents
print("\n🔍 STEP 1: Searching documents...")
docs = search_docs(question, k=3)
print(f"✅ Found {len(docs)} relevant documents")

# STEP 2: Prepare context
context = "\n\n---\n\n".join(docs)

# STEP 3: Generate answer using LLM
print("\n🤖 STEP 2: Generating answer...\n")

prompt = f"""
Based ONLY on this context, answer the question:

CONTEXT:
{context}

QUESTION: {question}

Instructions:
1. Use ONLY information from context
2. If not in context, say "Not found in documents"
3. Add citations naturally in your answer
4. Structure your answer well

Answer:
"""

# Call LM Studio directly
import requests
response = requests.post(
    "http://localhost:1234/v1/chat/completions",
    json={
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7,
        "max_tokens": 500
    }
)

if response.status_code == 200:
    answer = response.json()["choices"][0]["message"]["content"]
else:
    answer = f"Error: {response.status_code}"

# Show answer
print("\n" + "="*50)
print("📝 FINAL ANSWER:")
print("="*50)
print(answer)

# Word count
wc = count_words(str(answer))
print(f"\n📊 Word count: {wc}")

# Save output
with open("assignment_output.txt", "w", encoding="utf-8") as f:
    f.write("="*50 + "\n")
    f.write("AGENTIC RESEARCH ASSISTANT - ASSIGNMENT\n")
    f.write("="*50 + "\n\n")
    f.write(f"QUESTION: {question}\n\n")
    f.write(f"ANSWER:\n{answer}\n\n")
    f.write("-"*40 + "\n")
    f.write(f"STATISTICS:\n")
    f.write(f"- Word count: {wc}\n")
    f.write(f"- Documents retrieved: {len(docs)}\n")

print("\n💾 Output saved to: assignment_output.txt")
print("\n✅ ASSIGNMENT COMPLETE!")