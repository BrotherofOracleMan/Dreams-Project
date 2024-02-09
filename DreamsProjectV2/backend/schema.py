from pydantic import BaseModel
from datetime import datetime

class Dream(BaseModel):
    dream_id: int
    dream_title: str
    dream_description: str
    author_id: str

    class Config:
        from_attributes = True
