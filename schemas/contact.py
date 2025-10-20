from pydantic import BaseModel, EmailStr,Field, HttpUrl
from datetime import datetime


class ContactList(BaseModel):
    id: int
    name: str = Field(..., min_length=2, max_length=50)
    create_at: datetime

    class Config:
        from_attributes = True


class ContactBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    email: EmailStr
    url: HttpUrl | None = Field(default=None)
    gender: int = Field(..., strict=True, ge=0, le=2)
    message: str = Field(..., max_length=200)
    is_enabled: bool = Field(default=False)

    class Config:
        from_attributes = True


class ContactDelatil(ContactBase):
    id: int
    create_at: datetime

    class Config:
        from_attributes = True


class ContactCreate(ContactBase):
    pass