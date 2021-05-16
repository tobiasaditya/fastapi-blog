from fastapi import APIRouter
from fastapi.params import Depends
from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session
from project import schema, models, database

router = APIRouter(
    prefix="/project",
    tags=['Projects']
)

@router.post('/new')
def create_project(request:schema.Project, db:Session = Depends(database.get_db)):
    new_project = models.Project(title = request.title, due_date = request.due_date)
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return request

@router.get('/find')
def show_project_all(db:Session=Depends(database.get_db)):
    all_projects = db.query(models.Project).all()
    return all_projects

@router.get('/find/{id}')
def show_project_id(id:int, db:Session = Depends(database.get_db)):
    selected_project = db.query(models.Project).filter(models.Project.id == id).first()

    if not selected_project:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Project {id} not found.")

    return selected_project

@router.put('/update/{id}')
def update_project_id(id:int,request:schema.Project,db:Session = Depends(database.get_db)):
    #Search for projects' id
    selected_project = db.query(models.Project).filter(models.Project.id == id)

    if not selected_project.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Project {id} not found.")


    selected_project.update(dict(request))

    return {'status':f'project {id} updated'}



@router.delete('/delete/{id}')
def delete_project_id(id:int,db:Session = Depends(database.get_db)):
    selected_project = db.query(models.Project).filter(models.Project.id == id).first()

    if not selected_project:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Project {id} not found.")

    db.delete(selected_project)
    db.commit()

    return {'status':f'delete project_id {id} successful'}

