from dotenv import load_dotenv
import os
from sqlalchemy import Column, DateTime, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.orm import sessionmaker

load_dotenv('.env')

Base = declarative_base()


class Dream(Base):
    __tablename__ = 'dreams'
    id = Column(Integer, primary_key=True, index=True)
    dream_title = Column(String)
    dream_description = Column(String)
    author_id = Column(String)
    last_updated = Column(DateTime(timezone=True), onupdate=func.now())
    created = Column(DateTime(timezone=True), server_default=func.now())


DATABASE_URL = os.environ.get("DATABASE_URL")

engine = create_engine(DATABASE_URL)

Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
