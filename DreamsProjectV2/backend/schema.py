from pydantic import BaseModel
from datetime import datetime, date


class Dream(BaseModel):
    dream_id: int
    dream_title: str
    dream_description: str
    author_id: str

    class Config:
        from_attributes = True


class BeginAndLastDate(BaseModel):
    begin_date: date
    last_date: date
