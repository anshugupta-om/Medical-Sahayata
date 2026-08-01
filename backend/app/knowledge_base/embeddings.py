from pathlib import Path

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"


def get_embeddings():
    return HuggingFaceEmbeddings(
        model_name=MODEL_NAME
    )


def create_vector_store(chunks):
    embeddings = get_embeddings()

    vector_store = FAISS.from_documents(
        documents=chunks,
        embedding=embeddings,
    )

    return vector_store


def save_vector_store(vector_store, save_path: str):
    """
    Save the FAISS vector store to disk.
    """
    Path(save_path).mkdir(parents=True, exist_ok=True)
    vector_store.save_local(save_path)
   
def load_vector_store(load_path: str):
    """
    Load a saved FAISS vector store.
    """
    embeddings = get_embeddings()

    vector_store = FAISS.load_local(
        folder_path=load_path,
        embeddings=embeddings,
        allow_dangerous_deserialization=True,
    )

    return vector_store 