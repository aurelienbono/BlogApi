from sqlalchemy.orm import DeclarativeBase , sessionmaker
from sqlalchemy  import Column , Integer , String , Text , Date , DateTime
from config.config import engine

class Base(DeclarativeBase): 
    pass 


class Blog(Base):
    __tablename__ = 'blogs'
    id = Column(String, primary_key=True)
    title = Column(String)
    description = Column(String)
    owner = Column(String)
    read_count = Column(Integer)
    reading_time = Column(Integer)
    time_stamp = Column(Date) 

Base.metadata.create_all(engine)
SessionLocal = sessionmaker(autoflush=False , autocommit=False, bind=engine)