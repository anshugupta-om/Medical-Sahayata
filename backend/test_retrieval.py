from app.knowledge_base.embeddings import load_vector_store

# Load the saved FAISS vector store
vector_store = load_vector_store("../vector_db/faiss_index")

query = "What disease does the patient have?"

results = vector_store.similarity_search(query, k=3)

print(f"Retrieved {len(results)} document(s)\n")

for i, doc in enumerate(results, start=1):
    print("=" * 60)
    print(f"Result {i}")
    print("=" * 60)
    print(doc.page_content)
    print()
    
    
    
    
    