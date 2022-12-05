from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()
students = {
    1: {
        "name": "John",
        "age": 17,
        "year": "final year"
    }
}


class Student(BaseModel):
    name: str
    age: int
    year: str


@app.get("/")
def index():
    return {"message": "Server is app and running"}


# Path parameter
@app.get("/students/{student_id}")
def get_student_by_id(student_id: int = Path(None, description="The id of the student to be retrieved", gt=0)):
    return students[student_id]


# Query parameters
# Python Fast API does not allow for optional query params to come before required params,
# so we first put required params first and put asterix in-front of the optional param as variable required e.g.
# (*,name:Optional[str] = None ,test:int):
@app.get("/students")
def get_students_by_name(
        name: str = None):  # This makes it optional, or we can use Optional[str]=None (Is the recommended way)
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"message": "No data found"}


# Combining path params and query params
@app.get("/students-query/{student_id}")
def get_student_by_id_and_name(*, student_id_v: int, name: Optional[str] = None):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"message": "No data found"}


# Working with request bodies
@app.post("/students/create/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"message": "Student already exist"}
    students[student_id] = student
    return students[student_id]
