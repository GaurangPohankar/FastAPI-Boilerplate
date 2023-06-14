from typing import List, Optional
from pydantic import BaseModel


class BlogBase(BaseModel):
    title: str
    body: str
    published: Optional[bool] 
    
class Blog(BlogBase):
    class Config():
        orm_mode = True


class ShowBlog(BaseModel):
    title: str
    body:str
    class Config():
        orm_mode = True
