import os
from dotenv import load_dotenv
from pathlib import Path
from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


load_dotenv()
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
"""
SQLAlchemy configurations
"""
SQLALCHEMY_DATABASE_URI = 'mysql://root:6232@mysql:3306/test_guane?charset=utf8'

app = FastAPI()


engine = create_engine(SQLALCHEMY_DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
