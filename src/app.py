from fastapi import FastAPI
from http import HTTPStatus
from src.schemas import Message

app = FastAPI()


@app.get("/", status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {"message": "Olar mundooo"}
