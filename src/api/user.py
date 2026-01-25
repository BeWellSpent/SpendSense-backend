from fastapi import APIRouter, Depends, Body
from typing import Union, Annotated
from sqlmodel import Session
from db.session import get_session
from service.user_service import UserService

router = APIRouter()

@router.get("/")
async def read_root(session: Session = Depends(get_session)):
    return UserService().get_all(session)

@router.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None, session: Session = Depends(get_session)):
    return {"item_id": item_id, "q": q}
