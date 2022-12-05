from fastapi import FastAPI, Path

app = FastAPI()
students = {
    1: {
        "name": "John",
        "age": 17,
        "class": "final year"
    }
}


@app.get("/")
def index():
    return {"message": "Server is app and running"}


# Path parameter
@app.get("/students/{student_id}")
def get_student_by_id(student_id: int = Path(None, description="The id of the student to be retrieved", gt=0)):
    return students[student_id]


# Query parameters
@app.get("/students")
def get_students_by_name(name: str):
    for student_id in students:
        if students[student_id][name] == name:
            return students[student_id]
    return {"message": "No data found"}
