from fastapi import APIRouter

router = APIRouter()

leads = []

@router.post("/leads")

def create_lead(name:str,email:str):

    lead={
        "name":name,
        "email":email
    }

    leads.append(lead)

    return lead