from sqlalchemy.orm import Session

from ..schemas import blog as blogSchema
from ..models import blog as blogModel
from fastapi import HTTPException,status


def get_all(db: Session):
    blogs = db.query(blogModel.Blog).all()
    return blogs

def create(request: blogModel.Blog,db: Session):
    new_blog = blogModel.Blog(title=request.title, body=request.body,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def destroy(id:int,db: Session):
    blog = db.query(blogModel.Blog).filter(blogModel.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} not found")

    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'

def update(id:int,request:blogModel.Blog, db:Session):
    blog = db.query(blogModel.Blog).filter(blogModel.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} not found")

    blog.update(request)
    db.commit()
    return 'updated'

def show(id:int,db:Session):
    blog = db.query(blogModel.Blog).filter(blogModel.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with the id {id} is not available")
    return blog