from fastapi import FastAPI
from contextlib import asynccontextmanager
from week4.db import create_db_and_tables
from week4.student.router import router as student_router
from week4.course.router import router as course_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield
  
app = FastAPI(lifespan=lifespan)

app.include_router(student_router)
app.include_router(course_router)

#uv run uvicorn week4.main:app --reload