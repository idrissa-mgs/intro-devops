from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return "Hello! We are learning Docker"
