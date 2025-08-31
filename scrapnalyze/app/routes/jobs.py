from fastapi import APIRouter, Depends
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models import Job

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/jobs")
def job_list(request: Request, db: Session = Depends(get_db)):
    jobs = db.query(Job).all()
    return templates.TemplateResponse("jobs.html", {"request": request, "jobs": jobs})
