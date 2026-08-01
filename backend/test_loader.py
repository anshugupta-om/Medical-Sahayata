from app.knowledge_base.loader import load_medical_documents

documents = load_medical_documents("../data/medical_documents")

print(f"Loaded {len(documents)} pages.")

if documents:
    print("\nFirst Page Preview:\n")
    print(documents[0].page_content[:500])
    
    
