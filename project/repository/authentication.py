from fastapi import APIRouter
from fastapi.params import Depends
from fastapi import HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm.session import Session
from project import schema, models, database, hashing, token

router = APIRouter(
    prefix='/auth',
    tags=["Authentication"]
)

@router.post('/login', response_model=schema.Token)
def login(request:OAuth2PasswordRequestForm = Depends(), db:Session = Depends(database.get_db)):
    selected_user = db.query(models.User).filter(models.User.username == request.username).first()

    if not selected_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Username not found")
    
    if not hashing.verify_password(request.password,selected_user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Password was incorrect")
    
    # if all true, lanjut ke jwt
    created_token = token.create_access_token(data={'username':selected_user.username})
    return {"access_token": created_token, "token_type": "bearer"}
