from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from week4.db import get_session
from .model import Student
from .service import create_student, get_students, get_student_by_id

router = APIRouter(prefix="/students", tags=["students"])

@router.post("/", response_model=Student)
def create(student: Student, session: Session = Depends(get_session)):
    return create_student(session, student)

@router.get("/", response_model=list[Student])
def list_all(session: Session = Depends(get_session)):
    return get_students(session)

@router.get("/{student_id}", response_model=Student)
def get_one(student_id: int, session: Session = Depends(get_session)):
    student = get_student_by_id(session, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student