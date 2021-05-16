from pydantic import BaseModel

class Project(BaseModel):
    title : str
    due_date : str
    creator : str