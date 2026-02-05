# app/student/service.py
from sqlmodel import Session, select
from .model import Student  

def create_student(session: Session, student: Student):
    session.add(student)
    session.commit()
    session.refresh(student)
    return student 

def get_students(session: Session):
    return session.exec(select(Student)).all()

def get_student_by_id(session: Session, student_id: int):
    return session.get(Student, student_id)