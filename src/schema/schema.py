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
    
    

class UploadFiles(UploadFile) : 
    file : UploadFile