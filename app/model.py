from sqlalchemy import Column,Integer,String,TIMESTAMP,Boolean,text
from .database import Base

class Post(Base):
    __tablename__ = "post"

    id = Column(Integer,primary_key = True,nullable = False)
    title = Column(String,nullable = False)
    content = Column(String,nullable = False)
    published = Column(Boolean,insert_default=True)
    createdAt = Column(TIMESTAMP(timezone=True),
                       server_default=text('now()'))
