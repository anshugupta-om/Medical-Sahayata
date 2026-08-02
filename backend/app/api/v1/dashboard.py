from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.core.dependencies import get_current_user
from app.crud.report import get_latest_report

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get("/latest-report")
def latest_report(
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db),
):

    report = get_latest_report(
        db,
        current_user.id
    )

    if report is None:
        raise HTTPException(
            status_code=404,
            detail="No report found."
        )

    return {
        "summary": report.summary,
        "structured_data": report.structured_data,
        "uploaded_at": report.uploaded_at,
        "original_filename": report.original_filename
    }