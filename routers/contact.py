from fastapi import APIRouter
import schemas.contact as contact_schema
from datetime import datetime

router = APIRouter()

@router.get("/contacts",response_model=list[contact_schema.Contact])
async def lead_contact_all():
    dummy_data = datetime.now()
    return [contact_schema.Contact(
        id=1, name="スズキショウタ", email="aaa@gmail.com", url = "http:///", 
        gender="male", message="テスト", is_enabled= True, 
        create_at= dummy_data
        )]

@router.post("/contacts")
async def create_contact():
    pass

@router.get("/contacts/{id}")
async def read_contact():
    pass

@router.put("/contacts/{id}")
async def update_contact_id():
    pass

@router.delete("/contacts/{id}")
async def delete_contact_id():
    pass