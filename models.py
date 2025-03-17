from sqlalchemy import Column, Integer, String
from database import Base , engine

def create_table():
    Base.metadata.create_all(bind=engine)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(155), nullable=False) 
  
    email = Column(String(155), nullable=False)
