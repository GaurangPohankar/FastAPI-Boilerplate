from sqlalchemy import Column, Integer, String, ForeignKey
from ..database.database import Base
from sqlalchemy.orm import relationship


class Blog(Base):
    __tablename__ = "blog"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    published = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    creator = relationship("User", back_populates="blogs")

