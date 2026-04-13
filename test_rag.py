# test_rag.py
from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.utils import embedding_functions
import glob

print("🚀 Testing RAG Pipeline...")
print("="*40)

# 1. Load embedding model
print("\n1. Loading embedding model...")
model = SentenceTransformer('all-MiniLM-L6-v2')
print("   ✅ Model loaded")

# 2. Setup ChromaDB
print("\n2. Setting up ChromaDB...")
client = chromadb.PersistentClient(path="./chroma_db")

# Delete old if exists
try:
    client.delete_collection("my_docs")
    print("   Removed old collection")
except:
    pass

collection = client.create_collection(
    name="my_docs",
    embedding_function=embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )
)
print("   ✅ ChromaDB ready")

# 3. Load your TXT files
print("\n3. Loading your documents...")
files = glob.glob("knowledge_base/*.txt")
print(f"   📁 Found {len(files)} text files")

if len(files) == 0:
    print("   ❌ No files found! Run download_all_papers.py first")
    exit()

all_texts = []
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()
        all_texts.append(text[:2000])  # First 2000 chars only (faster)
print(f"   ✅ Loaded {len(all_texts)} documents")

# 4. Add to ChromaDB
print("\n4. Adding to vector database...")
collection.add(
    documents=all_texts,
    ids=[f"doc_{i}" for i in range(len(all_texts))]
)
print(f"   ✅ Added {len(all_texts)} documents to ChromaDB")

# 5. Test search
print("\n5. Testing search...")
test_question = "What is RAG?"
results = collection.query(
    query_texts=[test_question],
    n_results=2
)

print(f"\n📝 Question: {test_question}")
print(f"✅ Found {len(results['documents'][0])} relevant documents")

# Show first result preview
if results['documents'][0]:
    print("\n📄 Preview of first result:")
    print(results['documents'][0][0][:300])

print("\n" + "="*40)
print("🎉 RAG PIPELINE IS WORKING!")
print("✅ STEP 3 COMPLETE! Next: Run agents.py")