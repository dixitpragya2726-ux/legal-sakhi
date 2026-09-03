from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional

from legal_assistant import (
    generate_answer,
    get_helplines,
    draft_complaint,
    get_evidence_checklist,
    get_nearby_centers
)


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class QueryRequest(BaseModel):
    question: str
    language: str = "en"


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/ask")
def ask_question(request: QueryRequest):

    answer, sources = generate_answer(
        request.question,
        request.language
    )

    return {
        "answer": answer,
        "sources": sources
    }


@app.get("/helplines")
def helplines_endpoint():
    return {
        "helplines": get_helplines()
    }


@app.post("/draft-complaint")
def draft_complaint_endpoint(request: QueryRequest):

    draft, sources = draft_complaint(request.question)

    return {
        "draft": draft,
        "sources": sources
    }


@app.get("/evidence-checklist")
def evidence_checklist_endpoint():
    return {
        "checklist": get_evidence_checklist()
    }


@app.get("/nearby-help")
def nearby_help_endpoint(
    city: str = "",
    lat: Optional[float] = None,
    lng: Optional[float] = None
):
    centers = get_nearby_centers(
        city,
        user_lat=lat,
        user_lng=lng
    )

    return {
        "centers": centers
    }