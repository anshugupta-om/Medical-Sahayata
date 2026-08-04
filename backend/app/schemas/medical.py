from pydantic import BaseModel

class MedicalQuery(BaseModel):
    query: str
    language: str = "English"


class MedicalResponse(BaseModel):
    response: str