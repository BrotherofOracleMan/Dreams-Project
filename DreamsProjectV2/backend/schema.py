from pydantic import BaseModel
from datetime import datetime, date
from typing import Optional


class Dream(BaseModel):
    dream_id: Optional[int] = None
    dream_title: Optional[str] = None
    dream_description: Optional[str] = None
    author_id: Optional[str] = None

    class Config:
        from_attributes = True


class ItemUpdate(BaseModel):
    dream_title: Optional[str] = None
    dream_description: Optional[str] = None
    author_id: Optional[str] = None


class BeginAndLastDate(BaseModel):
    begin_date: date
    last_date: date
