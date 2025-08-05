from fastapi.testclient import TestClient
from src.api.flight_api import app

client = TestClient(app)

def test_get_flights():
    response = client.get("/flights")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    for flight in response.json():
        assert "tailNumber" in flight
        assert "make" in flight
        assert "model" in flight
        assert "owner" in flight
        assert isinstance(flight["tailNumber"], str)
        assert isinstance(flight["make"], str)
        assert isinstance(flight["model"], str)
        assert isinstance(flight["owner"], str)
