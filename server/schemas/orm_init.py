from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,DeclarativeBase
import os
from dotenv import load_dotenv
load_dotenv()


database_url=os.getenv("database_url")

engine = create_engine(database_url,echo=True)

class Base(DeclarativeBase):
    pass

SessionLocal=sessionmaker(bind=engine)
session=SessionLocal()
