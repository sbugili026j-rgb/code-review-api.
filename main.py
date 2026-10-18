from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Code Review API")


class ReviewRequest(BaseModel):
    code: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/review")
def review(request: ReviewRequest):
    lines = len(request.code.splitlines())
    return {"summary": f"Received {lines} line(s) of code"}