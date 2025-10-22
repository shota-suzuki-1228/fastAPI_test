from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
import cruds.contact as contact_crud
import schemas.contact as contact_schema
from database import get_db
from datetime import datetime

router = APIRouter()

@router.get("/contacts",response_model=list[contact_schema.ContactList])
async def lead_contact_all(db: AsyncSession = Depends(get_db)):
    return await contact_crud.get_contact_all(db=db)


@router.post("/contacts", response_model=contact_schema.ContactDelatil)
async def create_contact(body: contact_schema.ContactCreate, db: AsyncSession = Depends(get_db)):
    return await contact_crud.create_contact(db=db, contact=body)
    

@router.get("/contacts/{id}", response_model=contact_schema.ContactDelatil)
async def read_contact(id: int, db: AsyncSession = Depends(get_db)):
    contact = await contact_crud.get_contact(db=db, id=id)
    if contact is None:
        raise HTTPException(status_code=404, detail="そんな奴いねえよ！")
    return contact
    

@router.put("/contacts/{id}", response_model=contact_schema.ContactDelatil)
async def update_contact_id(id: int, body: contact_schema.ContactCreate, db: AsyncSession = Depends(get_db)):
    contact = await contact_crud.get_contact(db=db, id=id)
    if contact is None:
        raise HTTPException(status_code=404, detail="そんな奴いねえよ！")
    return await contact_crud.update_contact(db, body, original=contact)

@router.delete("/contacts/{id}")
async def delete_contact_id():
    pass