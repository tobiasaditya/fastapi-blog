from fastapi import FastAPI, HTTPException, status, APIRouter

from sqlalchemy.orm.session import Session
from project import schema, models, database
from project.repository import projects, user,authentication


app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

app.include_router(projects.router)
app.include_router(user.router)
app.include_router(authentication.router)
