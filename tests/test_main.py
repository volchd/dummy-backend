import sys
import os
sys.path.append('.')
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_layer():
    response = client.post("/layers/", json={"name": "Layer 1", "description": "First Layer"})
    assert response.status_code == 200
    assert response.json()["name"] == "Layer 1"

def test_create_building_block():
    # Assuming layer_id is 1 for testing purposes.
    response = client.post("/layers/1/blocks/", json={"name": "Block 1", "status": "NA"})
    assert response.status_code == 200
    assert response.json()["name"] == "Block 1"

def test_create_url():
    # Create a URL related to a layer
    response = client.post("/urls/", json={"url": "http://example.com", "related_id": 1, "related_table": "architecture_layers"})
    assert response.status_code == 200
    assert response.json()["url"] == "http://example.com"
    assert response.json()["related_id"] == 1
    assert response.json()["related_table"] == "architecture_layers"
