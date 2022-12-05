from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {"message": "Server is app and running"}
