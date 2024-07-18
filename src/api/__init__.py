from fastapi import FastAPI , Depends , File , UploadFile
from routes.routes import api_router


VERSION = 0




def start_applications(): 
  app  = FastAPI( 
                title='BLOG API ', 
                 version='0.1.1'
               ) 
  
  app.include_router(api_router)
  
  return app 
  
  
app  = start_applications()