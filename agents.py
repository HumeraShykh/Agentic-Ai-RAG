# agents.py
import autogen
import chromadb
import requests

print("🤖 Creating Agents...")
print("="*40)

# Test LM Studio connection
print("\n1. Testing LM Studio connection...")
try:
    response = requests.get("http://localhost:1234/v1/models")
    print("   ✅ LM Studio is running!")
except:
    print("   ❌ LM Studio not running! Start the server first.")
    exit()

# Connect to LM Studio
config_list = [{
    'model': 'phi-3.1-mini',
    'base_url': 'http://localhost:1234/v1',
    'api_key': 'not-needed',
}]

llm_config = {
    "config_list": config_list,
    "temperature": 0.7,
}

print("\n2. Connecting to ChromaDB...")
client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_collection("my_docs")
print("   ✅ Connected to ChromaDB")

# Search function
def search_docs(question, k=3):
    print(f"   🔍 Searching: {question[:50]}...")
    results = collection.query(query_texts=[question], n_results=k)
    return results['documents'][0]

# TOOL 1: Citation formatter
def add_citation(text, source):
    return f"{text}\n📖 Source: {source}"

# TOOL 2: Word counter
def count_words(text):
    return f"Word count: {len(text.split())}"

print("\n3. Creating Agents...")

# Agent 1: Planner
planner = autogen.AssistantAgent(
    name="Planner",
    system_message="You plan how to answer questions. Break down the task.",
    llm_config=llm_config,
)

# Agent 2: Answerer
answer_agent = autogen.AssistantAgent(
    name="Answerer",
    system_message="You answer using ONLY retrieved context. Add citations.",
    llm_config=llm_config,
)

# Agent 3: User Proxy
user_proxy = autogen.UserProxyAgent(
    name="UserProxy",
    human_input_mode="NEVER",
    code_execution_config=False,
)

# Register tools
user_proxy.register_function(
    function_map={
        "add_citation": add_citation,
        "count_words": count_words,
    }
)

print("\n✅ 3 Agents created:")
print("   1. Planner - makes plan")
print("   2. Answerer - generates answers")
print("   3. UserProxy - runs tools")
print("\n✅ 2 Tools created:")
print("   1. add_citation() - adds sources")
print("   2. count_words() - counts words")

print("\n" + "="*40)
print("🎉 AGENTS READY!")
print("Next: Run python main.py")