import json

from app.reports.report_extractor import ReportExtractor

extractor = ReportExtractor("../vector_db/faiss_index")

data = extractor.extract()

print(json.dumps(data, indent=4))