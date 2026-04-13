# check_install.py
try:
    import autogen
    print(f"✅ AutoGen version: {autogen.__version__}")
except:
    print("❌ AutoGen not installed")

try:
    import chromadb
    print(f"✅ ChromaDB version: {chromadb.__version__}")
except:
    print("❌ ChromaDB not installed")

try:
    from sentence_transformers import SentenceTransformer
    print("✅ Sentence Transformers ready")
except:
    print("❌ Sentence Transformers not installed")

print("\n🎉 If you see ✅ for all, installation successful!")