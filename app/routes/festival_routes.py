from fastapi import APIRouter
from app.services.festival_service import get_hindu_festivals

router = APIRouter()

@router.get("/festivals/{year}")
def get_festivals(year: int):
    return get_hindu_festivals(year)
