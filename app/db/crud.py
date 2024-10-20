from fastapi import HTTPException
from sqlalchemy import and_
from sqlalchemy.orm import Session
from app.db import models
from app.rest_api import schemas

NOT_FOUND_DETAIL = "object not found"


def create_architecture_layer(db: Session, layer: schemas.ArchitectureLayerCreate):
    db_layer = models.ArchitectureLayer(**layer.dict())
    db.add(db_layer)
    db.commit()
    db.refresh(db_layer)
    return db_layer
#get all architecture layers
def get_architecture_layers(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.ArchitectureLayer).offset(skip).limit(limit).all()
#get single architecture layer
def get_architecture_layer(db: Session, layer_id: int):
    layer = db.query(models.ArchitectureLayer).filter(models.ArchitectureLayer.id == layer_id).first()
        # If the layer doesn't exist, return a 404 error
    if layer is None:
        raise HTTPException(status_code=404, detail=NOT_FOUND_DETAIL)
    return layer

#update architecture layer
def update_architecture_layer(db: Session, layer_id: int, layer_update: schemas.ArchitectureLayerCreate):
    layer = db.query(models.ArchitectureLayer).filter(models.ArchitectureLayer.id == layer_id).first()    
    # If the layer doesn't exist, return a 404 error
    if layer is None:
        raise HTTPException(status_code=404, detail=NOT_FOUND_DETAIL)
    
    # Update the fields if new values are provided
    if layer_update.name is not None:
        layer.name = layer_update.name
    if layer_update.description is not None:
        layer.description = layer_update.description
    
    # Commit the changes to the database
    db.commit()
    db.refresh(layer)
    return layer

#delete architecture layer
def delete_architecture_layer(db: Session, layer_id: int):
    # Find the ArchitectureLayer by its ID
    layer = db.query(models.ArchitectureLayer).filter(models.ArchitectureLayer.id == layer_id).first()
    
    # If the layer does not exist, raise a 404 error
    if layer is None:
        raise HTTPException(status_code=404, detail=NOT_FOUND_DETAIL)
    
    # Delete the ArchitectureLayer from the database
    db.delete(layer)
    
    # Commit the changes to the database
    db.commit()


#create building block
def create_architecture_building_block(db: Session, block: schemas.ArchitectureBuildingBlockCreate, layer_id: int):
    db_block = models.ArchitectureBuildingBlock(**block.dict(), layer_id=layer_id)
    db.add(db_block)
    db.commit()
    db.refresh(db_block)
    return db_block

#get single building block
def get_architecture_building_block(db: Session, block_id: int):
    block = db.query(models.ArchitectureBuildingBlock).filter(models.ArchitectureBuildingBlock.id == block_id).first()
        # If the layer doesn't exist, return a 404 error
    if block is None:
        raise HTTPException(status_code=404, detail=NOT_FOUND_DETAIL)
    return block


#update building block
def update_architecture_building_block(db: Session, block: schemas.ArchitectureBuildingBlockCreate, block_id: int):
    db_block=db.query(models.ArchitectureBuildingBlock).filter(models.ArchitectureBuildingBlock.id == block_id).first()
     # If the layer doesn't exist, return a 404 error
    if db_block is None:
        raise HTTPException(status_code=404, detail=NOT_FOUND_DETAIL)
    
    # Update the fields if new values are provided
    if db_block.name is not None:
        db_block.name = block.name
    if db_block.description is not None:
        db_block.description = block.description
    if db_block.status is not None:
        db_block.status = block.status
    # Commit the changes to the database
    db.commit()
    db.refresh(db_block)
    return db_block

# get all architecture building blocks for an architecture layer
def get_all_architecture_building_block(db: Session,layer_id: int):
    layer =get_architecture_layer(db=db,layer_id=layer_id)
    return  db.query(models.ArchitectureBuildingBlock).filter(models.ArchitectureBuildingBlock.layer_id==layer_id).all()

#delete architecture lbuilding block
def delete_architecture_building_block(db: Session, layer_id: int, block_id :int):
    # Find the Architecture building block by its ID
    block = db.query(models.ArchitectureBuildingBlock).filter(and_(models.ArchitectureBuildingBlock.id == block_id, models.ArchitectureBuildingBlock.layer_id==layer_id)).first()
    
    # If the layer does not exist, raise a 404 error
    if block is None:
        raise HTTPException(status_code=404, detail=NOT_FOUND_DETAIL)
    
    # Delete the Architecture building block from the database
    db.delete(block)
    
    # Commit the changes to the database
    db.commit()

def create_url(db: Session, url: schemas.URLCreate, layer_id: int = None, building_block_id: int = None):
    db_url = models.URL(**url.dict(), layer_id=layer_id, building_block_id=building_block_id)
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return db_url

# You can add more CRUD functions here as needed for update/delete.
