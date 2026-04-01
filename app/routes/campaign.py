from fastapi import APIRouter
from app.services.campaign_service import add_campaign

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

@router.post("/campaigns/list")
def create_campaign(name:str, budget:int):
    return add_campaign(name, budget)