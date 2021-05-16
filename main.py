from fastapi import FastAPI
from project.schema import Project
app = FastAPI()


@app.post('/project')
def create_project(request:Project):
    return request

@app.get('/project')
def show_all():
    return {'result':'all projects'}

@app.get('/project/{id}')
def show_all(id:int):
    return {'result':f'project {id}'}

