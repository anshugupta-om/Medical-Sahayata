from app.crud.chat import create_chat
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from app.database.database import get_db
from app.crud.report import get_latest_report

from app.schemas.medical import MedicalQuery, MedicalResponse
from app.rag.rag_chain import MedicalRAG
from app.core.dependencies import get_current_user

router = APIRouter(
    prefix="/medical",
    tags=["Medical"]
)




@router.post("/consult", response_model=MedicalResponse)
def consult(
    request: MedicalQuery,
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
            detail="Please upload a medical report first."
        )

    rag = MedicalRAG(
        report.vector_store_path
    )

    answer = rag.ask(request.query)
    
    create_chat(
    db=db,
    user_id=current_user.id,
    report_id=report.id,
    question=request.query,
    answer=answer,
    )

    return MedicalResponse(
        response=answer
    )