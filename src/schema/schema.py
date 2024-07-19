from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from fastapi import UploadFile



class BlogBase(BaseModel):
    id: str
    title: str
    description: str
    owner: str
    read_count: int
    reading_time: int
    
    
    
class UserBase(BaseModel): 
    user_id  : str 
    username : str 
    firstname : str 
    email      : str 
    is_verified  : bool 
    created_at    : datetime 
    updated_at    : datetime 
    

    



class UploadFiles(UploadFile) : 
    file : UploadFile