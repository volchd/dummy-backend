from sqlalchemy.orm import Session
from app.db import models
from app.rest_api import schemas

def create_architecture_layer(db: Session, layer: schemas.ArchitectureLayerCreate):
    db_layer = models.ArchitectureLayer(**layer.dict())
    db.add(db_layer)
    db.commit()
    db.refresh(db_layer)
    return db_layer

def get_architecture_layers(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.ArchitectureLayer).offset(skip).limit(limit).all()

def create_architecture_building_block(db: Session, block: schemas.ArchitectureBuildingBlockCreate, layer_id: int):
    db_block = models.ArchitectureBuildingBlock(**block.dict(), layer_id=layer_id)
    db.add(db_block)
    db.commit()
    db.refresh(db_block)
    return db_block

def create_url(db: Session, url: schemas.URLCreate, layer_id: int = None, building_block_id: int = None):
    db_url = models.URL(**url.dict(), layer_id=layer_id, building_block_id=building_block_id)
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return db_url

# You can add more CRUD functions here as needed for update/delete.
