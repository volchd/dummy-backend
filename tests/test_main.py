import sqlite3
import sys
import os

import pytest
from sqlalchemy import text
sys.path.append('.')
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from fastapi.testclient import TestClient
from app.main import app
from app.db.database import get_db
client = TestClient(app)

@pytest.fixture(scope="session", autouse=True)
def database_connection():
    db = get_db()
    db = next(db)  # Get the actual database connection object
    try:
        db.execute(text("DELETE FROM architecture_layers"))
        db.execute(text("DELETE FROM architecture_building_blocks"))
        db.commit()
    except sqlite3.OperationalError:
        pass
    db.execute(text("VACUUM"))
    db.commit()
    db.execute(text("PRAGMA foreign_keys = ON"))
    db.commit()

#testing architecture layer object
def test_create_layer():
    response = client.post("/layers/", json={"name": "Layer 1", "description": "First Layer"})
    assert response.status_code == 200
    assert response.json()["name"] == "Layer 1"

def test_get_layer():
    response = client.get("/layers/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Layer 1"
    
    response = client.get("/layers/10")
    assert response.status_code == 404

def test_update_layer():
    response = client.put("/layers/1", json={"name": "Layer 1 updated", "description": "updated Layer"})
    assert response.status_code == 200
    assert response.json()["name"] == "Layer 1 updated"
    assert response.json()["description"] == "updated Layer"

    response = client.put("/layers/10", json={"name": "Layer 1 updated", "description": "updated Layer"})
    assert response.status_code == 404

def test_get_all_layer():
    client.post("/layers/", json={"name": "Layer 2", "description": "Second Layer"})
    response = client.get("/layers")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2

def test_delete_layer():
    response = client.delete("/layers/1")
    assert response.status_code == 204
    response = client.delete("/layers/2")
    assert response.status_code == 204

    response = client.delete("/layers/2")
    assert response.status_code == 404


''' 
def test_create_building_block():
    # Assuming layer_id is 1 for testing purposes.
    response = client.post("/layers/1/blocks/", json={
  "name": "Block 1",
  "description": "Block 1 description",
  "status": "NA"
})
    assert response.status_code == 200
    assert response.json()["name"] == "Block 1"

def test_create_url():
    # Create a URL related to a layer
    response = client.post("/urls/", json={"url": "http://example.com"})
    assert response.status_code == 200
    assert response.json()["url"] == "http://example.com"
    assert response.json()["related_id"] == 1
    assert response.json()["related_table"] == "architecture_layers"
'''