from pydantic import BaseModel


class MedicalQuery(BaseModel):
    query: str


class MedicalResponse(BaseModel):
    response: str