from fastapi import FastAPI, HTTPException
from http import HTTPStatus
from src.schemas import Message, User, UserPublic, UserDb, UserList

app = FastAPI()

database = []


@app.get("/", status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {"message": "Olar mundooo"}


@app.post(
    "/user/", response_model=UserPublic, status_code=HTTPStatus.CREATED
)  # contrato de saida
def create_user(user: User):  # contrato de entrada
    user_with_id = UserDb(**user.model_dump(), id=len(database) + 1)

    database.append(user_with_id)

    return user_with_id


@app.get("/user/", response_model=UserList)
def read_user():
    return {"users": database}


@app.put("/user/{user_id}", response_model=UserPublic)
def update_user(user_id: int, user: User):
    if user_id < 1 or user_id > len(database):
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="User not found")

    user_with_id = UserDb(**user.model_dump(), id=user_id)

    database[user_id - 1] = user_id

    return user_with_id


@app.delete("/user/{user_id}", response_model=Message)
def delete_user(user_id: int):
    if user_id < 1 or user_id > len(database):
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="User not found")

    del database[user_id - 1]

    return {"message": "User deleted"}
