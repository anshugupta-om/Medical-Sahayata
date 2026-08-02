from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

from app.core.config import settings
from app.knowledge_base.embeddings import load_vector_store


class ReportSummarizer:

    def __init__(self, vector_store_path: str):

        self.vector_store = load_vector_store(vector_store_path)

        self.llm = ChatOpenAI(
            api_key=settings.OPENAI_API_KEY,
            model="gpt-4o-mini",
            temperature=0
        )

        self.prompt = ChatPromptTemplate.from_template(
            """
You are an AI medical assistant.

Use ONLY the provided report.

Generate a structured summary with the following headings:

1. Patient Information
2. Hospital Information
3. Diagnosis
4. Chief Complaint
5. Laboratory Results
6. Prescribed Medicines
7. Doctor's Advice
8. Risk Level (Low / Medium / High)
9. Follow-up Recommendation

Context:
{context}
"""
        )

    def summarize(self):

        docs = self.vector_store.similarity_search("", k=10)

        context = "\n\n".join(
            doc.page_content
            for doc in docs
        )

        chain = self.prompt | self.llm

        response = chain.invoke(
            {
                "context": context
            }
        )

        return response.content