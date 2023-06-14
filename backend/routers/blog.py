from typing import List
from fastapi import APIRouter,Depends,status,HTTPException
from ..utils import oauth2

from ..schemas import blog as blogSchema
from ..schemas import user as userSchema

from ..database import database
from sqlalchemy.orm import Session
from ..service import blog as blogService

router = APIRouter(
    prefix="/blog",
    tags=['Blogs'],
    dependencies=[Depends(oauth2.get_current_user)]
) 

get_db = database.get_db

@router.get('/', response_model=List[blogSchema.ShowBlog])
def all(db: Session = Depends(get_db)):
    return blogService.get_all(db)


@router.post('/', status_code=status.HTTP_201_CREATED,)
def create(request: blogSchema.Blog, db: Session = Depends(get_db)):
    return blogService.create(request, db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id:int, db: Session = Depends(get_db)):
    return blogService.destroy(id,db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id:int, request: blogSchema.Blog, db: Session = Depends(get_db)):
    return blogService.update(id,request, db)


@router.get('/{id}', status_code=200, response_model=blogSchema.ShowBlog)
def show(id:int, db: Session = Depends(get_db)):
    return blogService.show(id,db)
