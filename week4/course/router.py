from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from week4.db import get_session
from .model import Course
from .service import create_course, get_courses, get_course_by_id

router = APIRouter(prefix="/courses", tags=["courses"])

@router.post('/', response_model=Course)
def create(course: Course, session: Session = Depends(get_session)):
    return create_course(session, course)

@router.get('/', response_model=list[Course])
def list_all(session: Session = Depends(get_session)):
    return get_courses(session)

@router.get('/{course_id}', response_model=Course)
def get_one(course_id: int, session: Session = Depends(get_session)):
    course = get_course_by_id(session, course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course