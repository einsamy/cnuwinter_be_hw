from typing import Optional
from pydantic import BaseModel, Field
from fastapi import APIRouter, HTTPException

students_router = APIRouter(prefix="/students", tags=["students"])

class Student(BaseModel):
    id: int
    name: str
    age: int

students = [
    Student(id=1, name='Alice', age=20),
    Student(id=2, name='Bob', age=22),
    Student(id=3, name='Charlie', age=21),
]

class StudentCreate(BaseModel):
    name: str = Field(..., example="Alice")
    age: int = Field(..., ge=0, example=20)

class StudentUpdate(BaseModel):
    name: str
    age: int = Field(..., ge=0)

class StudentPatch(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = Field(None, ge=0)


@students_router.get(
    '',
    status_code=200,
    summary="학생 목록 조회"
)
def get_students():
    return students


@students_router.get(
    '/{student_id}',
    status_code=200,
    responses={404: {"description": "Student not found"}},
    summary="학생 단일 조회"
)
def get_student_by_id(student_id: int):
    for student in students:
        if student.id == student_id:
            return student
    raise HTTPException(status_code=404, detail='Student not found')


@students_router.post(
    '',
    status_code=201,
    summary="학생 생성"
)
def create_student(payload: StudentCreate):
    student = Student(id=len(students)+1, **payload.model_dump())
    students.append(student)
    return student
@students_router.put(
    '/{student_id}',
    status_code=200,
    responses={404: {"description": "Student not found"}},
    summary="학생 전체 수정"
)
def update_student(student_id: int, payload: StudentUpdate):
    for student in students:
        if student.id == student_id:
            student = Student(id=student_id, **payload.model_dump())
            return student
    raise HTTPException(status_code=404, detail='Student not found')


@students_router.patch(
    '/{student_id}',
    status_code=200,
    responses={404: {"description": "Student not found"}},
    summary="학생 부분 수정"
)
def patch_student(student_id: int, payload: StudentPatch):
    for student in students:
        if student.id == student_id:
            if payload.name is not None:
                student.name = payload.name
            if payload.age is not None:
                student.age = payload.age
            return student
    raise HTTPException(status_code=404, detail='Student not found')


@students_router.delete(
    '/{student_id}',
    status_code=204,
    responses={404: {"description": "Student not found"}},
    summary="학생 삭제"
)
def delete_student(student_id: int):
    for student in students:
        if student.id == student_id:
            students.remove(student)
            return
    raise HTTPException(status_code=404, detail='Student not found')