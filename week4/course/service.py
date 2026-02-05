# app/course/service.py
from sqlmodel import Session, select
from .model import Course

def create_course(session: Session, course: Course):
    session.add(course)
    session.commit()
    session.refresh(course)
    return course 

def get_courses(session: Session):
    return session.exec(statement=select(Course)).all()

def get_course_by_id(session: Session, course_id: int):
    return session.get(Course, course_id)