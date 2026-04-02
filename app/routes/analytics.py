from fastapi import APIRouter

router = APIRouter()

analytics = {
    "campaigns": 4,
    "active_users": 25
}

@router.get("/analytics")
def get_analytics():
    return analytics