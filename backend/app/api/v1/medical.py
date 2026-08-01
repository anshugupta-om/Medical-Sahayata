from fastapi import APIRouter, Depends

from app.schemas.medical import MedicalQuery, MedicalResponse
from app.rag.rag_chain import MedicalRAG
from app.core.dependencies import get_current_user

router = APIRouter(
    prefix="/medical",
    tags=["Medical"]
)

rag = MedicalRAG()


@router.post("/consult", response_model=MedicalResponse)
def consult(
    request: MedicalQuery,
    current_user=Depends(get_current_user)
):
    answer = rag.ask(request.query)

    return MedicalResponse(
        response=answer
    )