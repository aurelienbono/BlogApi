from fastapi import FastAPI , Depends , File , UploadFile
from schema.schema import BlogBase , UploadFiles
from models.models import SessionLocal, Blog 
from sqlalchemy.orm import Session
from datetime import datetime
import shutil



VERSION = 0

app  = FastAPI( 
                title='BLOG API ', 
                 version='0.1.1'
               ) 

def get_db(): 
    
    db = SessionLocal()
    
    try : 
        yield db 
    finally : 
        db.close()



@app.get('/')
def root(): 
    return {"message":"Hello world"}


@app.get(f'/api/v{VERSION}/all_blog')
def get_all_blogs(db:Session = Depends(get_db)): 
    all_blogs = db.query(Blog).all()
    return all_blogs

@app.get(f'/api/v{VERSION}/blog/{{str_id}}')
def get_blogs( str_id:str, db: Session = Depends(get_db)): 
    blog_infos = db.query(Blog).filter(Blog.id==str_id).first()
    if blog_infos : 
        return blog_infos 
    return {'id': str_id, 'message': 'Blog Not Found'} 
    
@app.post(f'/api/v{VERSION}/create_post')
def create_post(blog: BlogBase, db: Session = Depends(get_db)): 
    blog_info = Blog(
        id=blog.id,
        title=blog.title, 
        description=blog.description,
        owner=blog.owner,
        read_count=blog.read_count,
        reading_time=blog.reading_time, 
        time_stamp=datetime.now().date()  # Keep it as a date object
    )
    
    db.add(blog_info)
    db.commit()
    db.refresh(blog_info)
    
    return {'id':blog_info.id , 'message':'Blog created'}

@app.delete(f'/api/v{VERSION}/del_blog/{{str_id}}')
def delete_blog(str_id:str, db:Session = Depends(get_db)) :
    deleted_blog = db.query(Blog).filter(Blog.id==str_id).first()
    
    db.delete(deleted_blog)
    db.commit()
    return { 'message':'Deleted Blogs'} 


@app.put(f'/api/v{VERSION}/update_blog/{{str_id}}')
def update_blog(str_id: str, blog: BlogBase, db: Session = Depends(get_db)):
    update_blog = db.query(Blog).filter(Blog.id == str_id).first()
    
    if update_blog:
        update_blog.id = blog.id
        update_blog.title = blog.title
        update_blog.description = blog.description
        update_blog.owner = blog.owner
        update_blog.read_count = blog.read_count
        update_blog.reading_time = blog.reading_time
        update_blog.time_stamp = datetime.now().date()
        
        db.commit()
        db.refresh(update_blog)
        
        return update_blog
    
    return {'id': str_id, 'message': 'Blog Not Found'}

