from sqlalchemy.ext.asyncio import AsyncSession
import schemas.contact as contact_schema
import models.contact as contact_model
from typing import List,Tuple
from sqlalchemy import select
from sqlalchemy.engine import Result
from datetime import datetime

async def create_contact(db: AsyncSession, contact: contact_schema.ContactCreate) -> contact_model.Contact:
    contact_data = contact.model_dump()
    if contact_data["url"] is not None:
        contact_data["url"] = str(contact_data["url"])

    db_contact = contact_model.Contact(**contact_data)

    db.add(db_contact)
    await db.commit()
    await db.refresh(db_contact)
    return db_contact

async def get_contact_all(db: AsyncSession) -> List[Tuple[int, str, datetime]]:
    result : Result = await db.execute(
        select(
            contact_model.Contact.id,
            contact_model.Contact.name,
            contact_model.Contact.create_at
        )
    )
    return result.all()

async def get_contact(db: AsyncSession, id:int) -> contact_model.Contact | None:
    query = select(contact_model.Contact).where(contact_model.Contact.id == id)
    result:Result = await db.execute(query)
    return result.scalars().first()