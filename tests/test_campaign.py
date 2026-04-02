from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_campaign():

    response = client.post("/campaigns")

    assert response.status_code == 200