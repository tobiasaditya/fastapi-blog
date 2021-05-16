from typing import List
from fastapi import APIRouter
from fastapi.params import Depends
from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session
from project import schema, models, database, hashing

router = APIRouter(
    prefix="/user",
    tags=['Users']
)

@router.post('/')
def create_user(request:schema.User, db:Session = Depends(database.get_db)):
    hashed_pass = hashing.get_password_hash(request.password)
    new_user = models.User(name = request.name,username = request.username, password = hashed_pass)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return request

@router.get('/', response_model= List[schema.showUser])
def show_user_all(db:Session=Depends(database.get_db)):
    all_users = db.query(models.User).all()
    return all_users

@router.get('/{id}',response_model= schema.showUser)
def show_user_id(id:int, db:Session = Depends(database.get_db)):
    selected_project = db.query(models.User).filter(models.User.id == id).first()

    if not selected_project:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User {id} not found.")

    return selected_project

# @router.put('/{id}')
# def update_project_id(id:int,request:schema.Project,db:Session = Depends(database.get_db)):
#     #Search for projects' id
#     selected_project = db.query(models.Project).filter(models.Project.id == id)

#     if not selected_project.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Project {id} not found.")


#     selected_project.update(dict(request))

#     return {'status':f'project {id} updated'}



# @router.delete('/{id}')
# def delete_project_id(id:int,db:Session = Depends(database.get_db)):
#     selected_project = db.query(models.Project).filter(models.Project.id == id).first()

#     if not selected_project:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Project {id} not found.")

#     db.delete(selected_project)
#     db.commit()

#     return {'status':f'delete project_id {id} successful'}

