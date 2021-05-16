from typing import Optional
from pydantic import BaseModel

class Project(BaseModel):
    title : str
    due_date : str

class User(BaseModel):
    name : str
    username : str
    password : str
    class Config():
        orm_mode = True

class showUser(BaseModel):
    name: str
    username : str
    class Config():
        orm_mode = True

class loginUser(BaseModel):
    username : str
    password : str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None