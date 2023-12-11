from fastapi import APIRouter
from model import Developer
import service

router = APIRouter()

@router.get("/cal")
async def get_developer_productivity(developer: Developer):
    return await service.get_developer_productivity(developer)