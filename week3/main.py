from fastapi import FastAPI
from week3.students_router import students_router

app = FastAPI()

@app.get("/")
def hello() :
	return "Hello, World!"

app.include_router(students_router)