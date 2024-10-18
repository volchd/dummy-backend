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
#-----------------------------------------

#testing building block object
def test_create_building_block():
    response = client.post("/layers/", json={"name": "Layer 1", "description": "First Layer"})
    layer_id=response.json()["id"]
    response = client.post(f"/layers/{layer_id}/blocks/", json={
  "name": "Block 1",
  "description": "Block 1 description",
  "status": "NA"
})
    assert response.status_code == 200
    assert response.json()["name"] == "Block 1"

def test_get_building_block():
    response = client.get("/layers/1/blocks/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Block 1"
    
    response = client.get("/layers/1/blocks/10")
    assert response.status_code == 404


def test_update_building_block():
    response = client.put("/layers/1/blocks/1", json={
  "name": "updated",
  "description": "updated",
  "status": "Defined"
})
    assert response.status_code == 200
    assert response.json()["name"] == "updated"
    assert response.json()["description"] == "updated"
    assert response.json()["status"] == "Defined"

    response = client.put("/layers/1/blocks/10", json={
  "name": "updated",
  "description": "updated",
  "status": "Defined"
})
    assert response.status_code == 404



def test_get_all_building_blocks():
    response = client.post("/layers/", json={"name": "all Layer 1", "description": "First Layer"})
    layer_id=response.json()["id"]
    client.post(f"/layers/{layer_id}/blocks/", json={
  "name": "all Block 1",
  "description": "all Block 1 description",
  "status": "NA"
})
    client.post(f"/layers/{layer_id}/blocks/", json={
  "name": "all Block 2",
  "description": "all Block 2 description",
  "status": "NA"
})
    response=client.get(f"/layers/{layer_id}/blocks/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    response=client.get("/layers/100/blocks/")
    assert response.status_code == 404



def test_delete_building_block():
    response=client.delete("/layers/100/blocks/1")
    assert response.status_code == 404
    response=client.delete("/layers/1/blocks/100")
    assert response.status_code == 404
    response=client.delete("/layers/1/blocks/1")
    assert response.status_code == 204
#---------------------------------------------------
''' 
def test_create_url():
    # Create a URL related to a layer
    response = client.post("/urls/", json={"url": "http://example.com"})
    assert response.status_code == 200
    assert response.json()["url"] == "http://example.com"
    assert response.json()["related_id"] == 1
    assert response.json()["related_table"] == "architecture_layers"
'''