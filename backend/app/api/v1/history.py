from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.core.dependencies import get_current_user
from app.crud.report import get_user_reports

router = APIRouter(
    prefix="/history",
    tags=["Report History"]
)


@router.get("/reports")
def report_history(
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db),
):

    reports = get_user_reports(
        db,
        current_user.id
    )

    return [
        {
            "id": str(report.id),
            "filename": report.original_filename,
            "uploaded_at": report.uploaded_at,
        }
        for report in reports
    ]