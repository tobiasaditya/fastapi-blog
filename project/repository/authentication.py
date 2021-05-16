from fastapi import APIRouter
from fastapi.params import Depends
from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session
from project import schema, models, database, hashing

router = APIRouter(
    prefix='/auth',
    tags=["Authentication"]
)

@router.post('/')
def login(request:schema.loginUser, db:Session = Depends(database.get_db)):
    selected_user = db.query(models.User).filter(models.User.username == request.username).first()

    if not selected_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Username not found")
    
    if not hashing.verify_password(request.password,selected_user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Password was incorrect")
    
    # if all true, lanjut ke jwt
    return {'status':'login success'}
