from fastapi import APIRouter

router = APIRouter()

@router.get("/contacts")
async def read_contact_all():
    pass

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