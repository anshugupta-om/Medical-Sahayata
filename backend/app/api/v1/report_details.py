from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.core.dependencies import get_current_user
from app.models.report import MedicalReport

router = APIRouter(
    prefix="/report",
    tags=["Report Details"]
)


@router.get("/{report_id}")
def report_details(
    report_id: str,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db),
):

    report = (
        db.query(MedicalReport)
        .filter(
            MedicalReport.id == report_id,
            MedicalReport.user_id == current_user.id,
        )
        .first()
    )

    if report is None:
        raise HTTPException(
            status_code=404,
            detail="Report not found."
        )

    return {
        "summary": report.summary,
        "structured_data": report.structured_data,
        "uploaded_at": report.uploaded_at,
        "filename": report.original_filename,
    }