from fastapi import APIRouter, Depends, File, UploadFile
from app.reports.upload import save_uploaded_file
from app.reports.process_report import process_uploaded_report
from app.core.dependencies import get_current_user
from app.reports.upload import save_uploaded_file
from pathlib import Path
from app.core.dependencies import get_current_user
from sqlalchemy.orm import Session
from fastapi import Depends, File, UploadFile
from app.reports.report_summary import ReportSummarizer
from app.reports.report_extractor import ReportExtractor
from app.crud.report import create_report, update_report_analysis

from app.database.database import get_db

router = APIRouter(
    prefix="/report",
    tags=["Medical Report"]
)


@router.post("/upload")
def upload_report(
    file: UploadFile = File(...),
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db),
):

    file_path = save_uploaded_file(file)

    result = process_uploaded_report(file_path)

    report = create_report(
        db=db,
        user_id=current_user.id,
        original_filename=file.filename,
        stored_filename=Path(file_path).name,
        file_path=file_path,
        vector_store_path=result["vector_path"],
    )

    
    summarizer = ReportSummarizer(
    result["vector_path"]
    )

    summary = summarizer.summarize()

    extractor = ReportExtractor(
        result["vector_path"]
    )

    structured_data = extractor.extract()

    update_report_analysis(
        db=db,
        report_id=report.id,
        summary=summary,
        structured_data=structured_data,
    )
    
    return {
    "message": "Report uploaded successfully",
    "pages": result["pages"],
    "chunks": result["chunks"],
    "summary": summary,
    "structured_data": structured_data,
   }