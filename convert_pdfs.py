# convert_pdfs.py
import PyPDF2
import os
from glob import glob

print("="*50)
print("PDF to TXT Converter for Assignment")
print("="*50)

# Folders create karo
os.makedirs("pdfs", exist_ok=True)
os.makedirs("knowledge_base", exist_ok=True)

# Saari PDFs dhundo
pdf_files = glob("pdfs/*.pdf")

if len(pdf_files) == 0:
    print("\n No PDFs found in 'pdfs' folder!")
    print("   Please download the 20 papers first.")
    exit()

print(f"\n Found {len(pdf_files)} PDF files")
print(f" Need 20 documents - You have {len(pdf_files)}")

# Convert each PDF
converted = 0
for pdf_file in pdf_files:
    try:
        # Read PDF
        with open(pdf_file, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            
            # Extract text from all pages
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
            
            # Save as TXT
            base_name = os.path.basename(pdf_file).replace('.pdf', '.txt')
            txt_path = os.path.join("knowledge_base", base_name)
            
            with open(txt_path, 'w', encoding='utf-8') as txt_file:
                txt_file.write(text)
            
            print(f"   ✅ Converted: {base_name}")
            converted += 1
            
    except Exception as e:
        print(f"   ❌ Failed: {os.path.basename(pdf_file)} - {e}")

print("\n" + "="*50)
print(f"📊 SUMMARY:")
print(f"   ✅ Converted: {converted} files")
print(f"   📁 Location: knowledge_base/")
print("="*50)

# Verify we have 20 documents
txt_files = glob("knowledge_base/*.txt")
print(f"\n📚 Total text files in knowledge_base: {len(txt_files)}")

if len(txt_files) >= 20:
    print("🎉 PERFECT! You have 20+ documents for your RAG system!")
else:
    print(f"⚠️ You need {20 - len(txt_files)} more documents")