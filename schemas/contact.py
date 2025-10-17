from pydantic import BaseModel, EmailStr,Field, HttpUrl
from datetime import datetime


class Contact(BaseModel):
    id: int 
    name: str = Field(..., min_length=2, max_length=50)
    email: EmailStr
    url: HttpUrl | None = Field(default=None)
    gender: int = Field(..., strict=True, ge=0, le=2)
    message: str = Field(..., max_length=200)
    is_enabled: bool = Field(default=False)
    create_at: datetime