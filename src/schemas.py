from pydantic import BaseModel, EmailStr

class Message(BaseModel):
    message:str


class User(BaseModel):
    username: str
    email: EmailStr
    password: str