from app.knowledge_base.loader import load_medical_documents
from app.knowledge_base.splitter import split_documents

documents = load_medical_documents("../data/medical_documents")
chunks = split_documents(documents)

print(f"Loaded Pages: {len(documents)}")
print(f"Generated Chunks: {len(chunks)}")

if chunks:
    print("\nFirst Chunk:\n")
    print(chunks[0].page_content)