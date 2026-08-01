from app.rag.rag_chain import MedicalRAG

rag = MedicalRAG()

question = "What medicine is prescribed to the patient?"

answer = rag.ask(question)

print("\nQuestion:\n")
print(question)

print("\nAnswer:\n")
print(answer)