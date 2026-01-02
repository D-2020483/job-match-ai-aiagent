from fastapi import FastAPI
from app.ai_agent import match_cover_letter
from fastapi.middleware.cors import CORSMiddleware


from app.schemas import CoverLetterMatchRequest

app = FastAPI(
    title="Cover Letter Match AI",
    description="AI-powered cover letter evaluation system",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/cover-letter/match")
def cover_letter_match(request: CoverLetterMatchRequest):
    ai_result = match_cover_letter(
        request.job_description,
        request.education,
        request.cover_letter
    )

    return {
        "status": "success",
        "cover_letter_match": ai_result
    }

# Run:
# python -m uvicorn app.main:app --reload
