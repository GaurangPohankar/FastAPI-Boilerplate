from sqlalchemy import Column, Integer, String, ForeignKey
from ..database.database import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
 
    blogs = relationship('Blog', back_populates="creator")