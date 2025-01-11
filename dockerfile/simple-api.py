from fastapi import FastAPI
import os

NAME = os.environ.get('NAME')

app = FastAPI()


@app.get("/")
def read_root():
    return f"Hello {NAME}! We are learning Docker"
