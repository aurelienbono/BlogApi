

from sqlalchemy import Column , String , Integer , DateTime , Boolean
from sqlalchemy.orm import  sessionmaker
from blogs import Base , SessionLocal
from config.config import engine


class Users(Base): 
    __tablename__ = 'users' 
    
    Column('user_id',String(30),  primary_key=True, unique=True , nullable=False)
    Column('username', String(20), unique=True, nullable=False)
    Column('firstname', String(20))
    Column('lastname',String(20))
    Column('email', String(20))
    Column('is_verified', Boolean)
    Column('created_at', DateTime)
    Column('updated_at', DateTime)
    
    
    
Base.metadata.create_all()
SessionLocal = sessionmaker(bind=engine ,autoflush=False )

