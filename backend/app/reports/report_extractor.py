import json

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

from app.core.config import settings
from app.knowledge_base.embeddings import load_vector_store


class ReportExtractor:

    def __init__(self, vector_store_path: str):

        self.vector_store = load_vector_store(vector_store_path)

        self.llm = ChatOpenAI(
            api_key=settings.OPENAI_API_KEY,
            model="gpt-4o-mini",
            temperature=0
        )

        self.prompt = ChatPromptTemplate.from_template("""
You are an AI medical report analyzer.

Use ONLY the provided report.

Return ONLY valid JSON with these fields:

- patient_name
- age
- gender
- hospital
- doctor
- diagnosis
- chief_complaint
- medicines (array)
- laboratory_results (object)
- risk_level
- follow_up

Context:
{context}
""")
        
    def extract(self):

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
        
        print("\n========== LLM RESPONSE ==========\n")
        print(response.content)
        print("\n=================================\n")

        content = response.content.strip()

        # Remove Markdown code fences if present
        if content.startswith("```json"):
            content = content.replace("```json", "", 1)

        if content.startswith("```"):
            content = content.replace("```", "", 1)

        if content.endswith("```"):
            content = content[:-3]

        content = content.strip()

        return json.loads(content)