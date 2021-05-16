from pydantic import BaseModel

class Project(BaseModel):
    title : str
    due_date : str

class User(BaseModel):
    name : str
    username : str
    password : str

class showUser(BaseModel):
    name: str
    username : str
    class Config():
        orm_mode = True

class loginUser(BaseModel):
    username : str
    password : str

    