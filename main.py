from fastapi import FastAPI
from fastapi.params import Depends
from sqlalchemy.orm.session import Session
from project import schema, models, database


app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

@app.post('/project')
def create_project(request:schema.Project, db:Session = Depends(database.get_db)):
    new_project = models.Project(title = request.title, due_date = request.due_date)
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return request

@app.get('/project')
def show_project_all(db:Session=Depends(database.get_db)):
    all_projects = db.query(models.Project).all()
    return all_projects

@app.get('/project/{id}')
def show_project_id(id:int, db:Session = Depends(database.get_db)):
    selected_project = db.query
    return {'result':f'project {id}'}

