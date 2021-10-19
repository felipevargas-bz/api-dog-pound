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
SQLALCHEMY_DATABASE_URI = 'mysql://{0}:{1}@{2}:{3}/{4}?charset=utf8'.format(
    os.getenv("MYSQL_USER"),
    os.getenv("MYSQL_PASSWORD"),
    os.getenv("MYSQL_HOST"),
    os.getenv("MYSQL_PORT"),
    os.getenv("MYSQL_DATABASE")
)


app = FastAPI()


engine = create_engine(SQLALCHEMY_DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
