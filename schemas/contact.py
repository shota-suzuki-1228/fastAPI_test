from pydantic import BaseModel,Field
from datetime import datetime


class Contact(BaseModel):
    id: int
    name: str
    email: str
    url: str
    gender: str
    message: str
    is_enabled: bool
    create_at: datetime