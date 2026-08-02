from app.reports.report_summary import ReportSummarizer

vector_store_path = "../vector_db/faiss_index"

summarizer = ReportSummarizer(vector_store_path)

summary = summarizer.summarize()

print(summary)