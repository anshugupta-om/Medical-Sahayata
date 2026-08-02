from sqlalchemy.orm import Session

from app.models.report import MedicalReport


def create_report(
    db: Session,
    user_id,
    original_filename: str,
    stored_filename: str,
    file_path: str,
    vector_store_path: str,
):
    report = MedicalReport(
        user_id=user_id,
        original_filename=original_filename,
        stored_filename=stored_filename,
        file_path=file_path,
        vector_store_path=vector_store_path,
    )

    db.add(report)
    db.commit()
    db.refresh(report)

    return report

def update_report_analysis(
    db: Session,
    report_id,
    summary: str,
    structured_data: dict,
):
    report = (
        db.query(MedicalReport)
        .filter(MedicalReport.id == report_id)
        .first()
    )

    if report:

        report.summary = summary
        report.structured_data = structured_data

        db.commit()
        db.refresh(report)

    return report

def get_latest_report(db: Session, user_id):
    return (
        db.query(MedicalReport)
        .filter(MedicalReport.user_id == user_id)
        .order_by(MedicalReport.uploaded_at.desc())
        .first()
    )
    
    
def get_user_reports(db: Session, user_id):
    return (
        db.query(MedicalReport)
        .filter(MedicalReport.user_id == user_id)
        .order_by(MedicalReport.uploaded_at.desc())
        .all()
    )
