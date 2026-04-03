from pydantic import BaseModel

class Campaign(BaseModel):

    name: str
    budget: int