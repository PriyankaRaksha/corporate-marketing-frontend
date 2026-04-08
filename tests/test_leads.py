from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_lead():

    response = client.post("/leads")

    assert response.status_code == 200