from fastapi import APIRouter
from app.services.user_service import add_user

router = APIRouter()

@router.get("/analytics")

def analytics():

    data = {
        "campaigns": 10,
        "leads": 120
    }

    return data
