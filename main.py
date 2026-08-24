from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from legal_assistant import generate_answer, get_helplines, draft_complaint, get_evidence_checklist


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    question: str

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/ask")
def ask_question(request: QueryRequest):
    answer, sources = generate_answer(request.question)
    return {"answer": answer, "sources": sources}

@app.get("/helplines")
def helplines_endpoint():
    return {"helplines": get_helplines()}

@app.post("/draft-complaint")
def draft_complaint_endpoint(request: QueryRequest):
    draft, sources = draft_complaint(request.question)
    return {"draft": draft, "sources": sources}

@app.get("/evidence-checklist")
def evidence_checklist_endpoint():
    return {"checklist": get_evidence_checklist()}