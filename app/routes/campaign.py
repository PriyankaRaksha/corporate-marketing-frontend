from fastapi import APIRouter

router = APIRouter()

campaigns = []

@router.post("/campaigns")
def create_campaign(name:str, budget:int):
    campaign = {
        "name": name,
        "budget": budget
    }
    campaigns.append(campaign)
    return campaign