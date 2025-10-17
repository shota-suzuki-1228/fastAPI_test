from fastapi import APIRouter
import schemas.contact as contact_schema
from datetime import datetime

router = APIRouter()

@router.get("/contacts",response_model=list[contact_schema.Contact])
async def lead_contact_all():
    dummy_data = datetime.now()
    return [contact_schema.Contact(
        id=1, name="スズキショウタ", email="aaa@gmail.com", url = "https://www.example-nonexistent-domain-xyz1234.com/this-page-does-not-exist", 
        gender=2, message="テスト", is_enabled= True, 
        create_at= dummy_data
        )]

@router.post("/contacts", response_model=contact_schema.Contact)
async def create_contact(body: contact_schema.Contact):
    return contact_schema.Contact(**body.model_dump())
    

@router.get("/contacts/{id}")
async def read_contact():
    pass

@router.put("/contacts/{id}")
async def update_contact_id():
    pass

@router.delete("/contacts/{id}")
async def delete_contact_id():
    pass