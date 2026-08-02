from pathlib import Path

from app.knowledge_base.loader import load_medical_documents
from app.knowledge_base.splitter import split_documents
from app.knowledge_base.embeddings import (
    create_vector_store,
    save_vector_store,
)


def process_uploaded_report(file_path: str):
    """
    Process an uploaded PDF:
    - Load
    - Split
    - Generate embeddings
    - Save FAISS index
    """

    pdf_path = Path(file_path)

    # Load the uploaded PDF
    documents = load_medical_documents(str(pdf_path.parent))

    # Keep only the uploaded file
    documents = [
        doc for doc in documents
        if Path(doc.metadata["source"]).name == pdf_path.name
    ]

    # Split into chunks
    chunks = split_documents(documents)

    # Create vector store
    vector_store = create_vector_store(chunks)

    # Save vector index
    index_path = Path("../vector_db") / pdf_path.stem

    save_vector_store(
        vector_store,
        str(index_path)
    )

    return {
        "pages": len(documents),
        "chunks": len(chunks),
        "vector_path": str(index_path)
    }