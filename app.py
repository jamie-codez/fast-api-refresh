from fastapi import FastAPI

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
def get_student_by_id(student_id: int):
    return students[student_id]
