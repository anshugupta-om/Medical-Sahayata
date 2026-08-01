from app.knowledge_base.loader import load_medical_documents
from app.knowledge_base.splitter import split_documents
from app.knowledge_base.embeddings import (
    create_vector_store,
    save_vector_store,
)

documents = load_medical_documents("../data/medical_documents")
chunks = split_documents(documents)

vector_store = create_vector_store(chunks)

save_vector_store(
    vector_store,
    "../vector_db/faiss_index"
)

print(f"Loaded Pages: {len(documents)}")
print(f"Chunks: {len(chunks)}")
print("FAISS vector store created and saved successfully!")