from fastapi import APIRouter,Depends
from sqlalchemy.ext.asyncio import AsyncSession
import cruds.contact as contact_crud
import schemas.contact as contact_schema
from database import get_db
from datetime import datetime

router = APIRouter()

@router.get("/contacts",response_model=list[contact_schema.ContactList])
async def lead_contact_all():
    dummy_data = datetime.now()
    return [contact_schema.Contact(
        id=1, name="スズキショウタ", email="aaa@gmail.com", url = "https://www.example-nonexistent-domain-xyz1234.com/this-page-does-not-exist", 
        gender=2, message="テスト", is_enabled= True, 
        create_at= dummy_data
        )]

@router.post("/contacts", response_model=contact_schema.ContactCreate)
async def create_contact(body: contact_schema.ContactCreate, db: AsyncSession = Depends(get_db)):
    return await contact_crud.create_contact(db=db, contact=body)
    

@router.get("/contacts/{id}")
async def read_contact():
    pass

@router.put("/contacts/{id}")
async def update_contact_id():
    pass

@router.delete("/contacts/{id}")
async def delete_contact_id():
    pass