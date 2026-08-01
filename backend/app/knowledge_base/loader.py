from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader


def load_medical_documents(data_dir: str):
    """
    Load all PDF documents from the specified directory.
    """
    documents = []

    pdf_files = Path(data_dir).glob("*.pdf")

    for pdf_file in pdf_files:
        loader = PyPDFLoader(str(pdf_file))
        documents.extend(loader.load())

    return documents