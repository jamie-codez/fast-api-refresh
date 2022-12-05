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


class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None


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


# Put methods : When the method is left as update_student(student_id: int, student: UpdateStudent) it updates the
# provided field and puts null in the others ; Lets solve this as below
@app.put("/students/update/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"message": "Student does not exist"}
    if student.name is not None:
        students[student_id].name = student.name
    if student.age is not None:
        students[student_id].age = student.age
    if students[student_id].year is not None:
        students[student_id].year = student.year
    # students[student_id] = student
    return students[student_id]
