from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

from app.knowledge_base.embeddings import load_vector_store
from app.core.config import settings


class MedicalRAG:

    def __init__(self):

        self.vector_store = load_vector_store("../vector_db/faiss_index")

        self.llm = ChatOpenAI(
            api_key=settings.OPENAI_API_KEY,
            model="gpt-4o-mini",
            temperature=0
        )

        self.prompt = ChatPromptTemplate.from_template(
            """
You are Medical Sahayata, an AI healthcare assistant.

Use ONLY the information provided in the context below.

If the answer is not available in the context, reply exactly:

"I couldn't find reliable medical information in the provided documents."

Always end your response with:

"This information is for educational purposes only and is not a substitute for professional medical advice."

Context:
{context}

Question:
{question}
"""
        )

    def ask(self, question: str):

        docs = self.vector_store.similarity_search(question, k=3)

        context = "\n\n".join(
            [doc.page_content for doc in docs]
        )

        chain = self.prompt | self.llm

        response = chain.invoke(
            {
                "context": context,
                "question": question
            }
        )

        return response.content