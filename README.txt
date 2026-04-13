================================================================
AGENTIC ACADEMIC ASSISTANT - ASSIGNMENT
================================================================
Student Name: [Apna naam likho]
Subject: Advanced NLP
Assignment: Build an Agentic AI Research Assistant with RAG + Tools

================================================================
HOW TO RUN THE SYSTEM (STEP BY STEP)
================================================================

---------
STEP 1: Open Project Folder
---------
Open VS Code and open this folder:
D:\MS\ANLP\Assignment 5\agentic_rag_assignment\

---------
STEP 2: Activate Virtual Environment
---------
Open TERMINAL in VS Code (Ctrl + `) and type:
venv\Scripts\activate

You should see (venv) at the beginning of the terminal line.

---------
STEP 3: Start LM Studio Server
---------
1. Open LM Studio application
2. Click on "Local Inference Server" tab (left side, rocket icon 🚀)
3. Click "Start Server" button
4. Wait for green message: "Server running on http://localhost:1234"
5. Keep LM Studio OPEN (minimize it)

---------
STEP 4: Run the Assignment
---------
In the terminal, type:
python assignment_final.py

---------
STEP 5: Ask a Question
---------
When prompted "Enter your question:", type any question like:
- Compare RAG and fine-tuning in LLMs with examples.
- What is RAG?
- Explain fine-tuning with examples.

OR press Enter to use default question.

---------
STEP 6: View Answer
---------
Wait 30-60 seconds for the answer. The answer will include:
- Definitions of RAG and Fine-tuning
- Comparison Table
- Examples
- Citations/References
- Word Count

---------
STEP 7: Check Output File
---------
Answer is automatically saved in:
assignment_output.txt

You can open this file to see the saved output.

================================================================
TROUBLESHOOTING (Agar kuch kaam nahi kare)
================================================================

Problem 1: "No module named 'chromadb'"
Solution: In terminal type:
pip install chromadb sentence-transformers requests

Problem 2: "LM Studio connection error"
Solution: Make sure LM Studio server is started (green message)

Problem 3: "Collection 'my_docs' not found"
Solution: First run: python test_rag.py (to create database)

Problem 4: (venv) not showing
Solution: Type in terminal:
venv\Scripts\activate

================================================================
FILES IN THIS FOLDER
================================================================

assignment_final.py   - Main code (3 Agents, 2 Tools, RAG)
assignment_output.txt - Output file (auto-generated)
README.txt           - This file (instructions)
knowledge_base/      - Folder with 20 documents
chroma_db/           - Vector database (auto-created)
venv/                - Virtual environment with packages

================================================================
SYSTEM REQUIREMENTS FULFILLED
================================================================

✅ 3 Agents: Planner, Retriever, Answer Agent
✅ 2 Tools: Citation Formatter, Word Counter
✅ RAG Pipeline: ChromaDB + Sentence Transformers
✅ 20+ Documents: Research papers on RAG, Fine-tuning, LLMs
✅ Local LLM: LM Studio with Phi-3.1-mini model
✅ Structured Answer: Definitions, Comparison Table, Examples, Citations

================================================================
SAMPLE OUTPUT (Expected)
================================================================

QUESTION: Compare RAG and fine-tuning in LLMs with examples.

ANSWER:
## 1. Definition of RAG
RAG is a technique that combines information retrieval with text generation...

## 2. Definition of Fine-tuning
Fine-tuning is the process of training a pre-trained LLM on specific data...

## 3. Comparison Table
| Feature | RAG | Fine-tuning |
|---------|-----|-------------|
| How it works | Retrieves external data | Modifies model parameters |
| Training needed | No | Yes |
...

## 4. Example Use Cases
RAG Example: Customer support with product manuals
Fine-tuning Example: Medical note summarizer

## 5. References
Document_1, Document_2, Document_3

================================================================
PRESENTATION TIPS
================================================================

When presenting to teacher:
1. Show LM Studio server is running (green message)
2. Show terminal with (venv) active
3. Run: python assignment_final.py
4. Type the assignment question
5. Show the output with comparison table
6. Explain: "Ye 3 agents hain - Planner, Retriever, Answerer"
7. Explain: "Ye 2 tools hain - Citation Formatter aur Word Counter"

================================================================
SUBMISSION CHECKLIST
================================================================

[ ] assignment_final.py
[ ] assignment_output.txt  
[ ] README.txt
[ ] requirements.txt
[ ] knowledge_base/ folder (20 documents)
[ ] chroma_db/ folder (will be created when run)

================================================================
END OF INSTRUCTIONS
================================================================