from fastapi import FastAPI
import os

app = FastAPI()

# Récupérer la variable d'environnement
GREETING_NAME = os.getenv("GREETING_NAME", "World")

@app.get("/")
def read_root():
    return f"Hello {GREETING_NAME}! We are learning Docker"
