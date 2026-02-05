from typing import Optional, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from app.student.model import Student

class Course(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    course_name: str
    credit: int
    description: str
    
    instructor_id: Optional[int] = Field(default=None, foreign_key="student.id")
    instructor: Optional["Student"] = Relationship(back_populates="courses")