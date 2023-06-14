from fastapi import APIRouter, FastAPI, Depends, status, Response

from ..schemas import user as userSchema
from ..models import user as userModel
from typing import List
from ..database.database import engine, SessionLocal, get_db
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from ..utils.hashing import Hash

router = APIRouter(
    prefix="/user",
    tags=['Users']
)
 
@router.post("/", response_model=userSchema.ShowUser)
async def create_user(request: userSchema.User, db: Session = Depends(get_db)):
    new_user = userModel.User(name=request.name,email=request.email,password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user



@router.get("/" , response_model=List[userSchema.ShowUser]) 
async def get_all_user(db: Session = Depends(get_db)):
    users = db.query(userModel.User).all()
    return users


@router.get("/{id}" , response_model=userSchema.ShowUser)
async def get_user(id, response:Response ,db: Session = Depends(get_db)):
    user = db.query(userModel.User).filter(userModel.User.id == id).first()
    if not user:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'detail': "User with id {id} is not available"}
    return user


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update_user(id: int, request: userSchema.User, db: Session = Depends(get_db)):
    db.query(userModel.User).filter(userModel.User.id == id).update(request.dict())
    db.commit()
    return 'updated'


@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
async def all(id, response:Response ,db: Session = Depends(get_db)):
    user = db.query(userModel.User).filter(userModel.User.id == id).delete(synchronize_session=False)
    db.commit()
    return 'deleted'

