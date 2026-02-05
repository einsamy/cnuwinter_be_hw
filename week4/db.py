from sqlmodel import SQLModel, create_engine, Session
import week4.student.model 
import week4.course.model 

engine=create_engine("sqlite:///database.db")

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session