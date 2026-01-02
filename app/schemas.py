from pydantic import BaseModel

class CoverLetterMatchRequest(BaseModel):
    job_description: str
    education: str
    cover_letter: str


class CoverLetterMatchResponse(BaseModel):
    status: str
    cover_letter_match: dict
