from fastapi import APIRouter

router = APIRouter()

analytics = {
    "campaigns": 4,
    "active_users": 25
}

@router.get("/analytics")
def analytics():

    data = {
        "campaigns": 10,
        "leads": 120
    }

    return data