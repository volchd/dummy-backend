from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import models
from app.rest_api import schemas
from app.db import crud
from app.db.database import engine, Base, get_db


router_layers = APIRouter(
    prefix='/layers',
    tags=['Architecture Layers']
)

@router_layers.post("/", response_model=schemas.ArchitectureLayer)
def create_architecture_layer(layer: schemas.ArchitectureLayerCreate, db: Session = Depends(get_db)):
    return crud.create_architecture_layer(db=db, layer=layer)

@router_layers.get("/", response_model=List[schemas.ArchitectureLayer])
def read_architecture_layers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_architecture_layers(db=db, skip=skip, limit=limit)


@router_layers.post("/{layer_id}/blocks/", response_model=schemas.ArchitectureBuildingBlock)
def create_architecture_building_block(layer_id: int, block: schemas.ArchitectureBuildingBlockCreate, db: Session = Depends(get_db)):
    return crud.create_architecture_building_block(db=db, block=block, layer_id=layer_id)

@router_layers.post("/{layer_id}/urls/", response_model=schemas.URL)
def create_layer_url(layer_id: int, url: schemas.URLCreate, db: Session = Depends(get_db)):
    return crud.create_url(db=db, url=url, layer_id=layer_id)

'''
@router_layers.post("/blocks/{block_id}/urls/", response_model=schemas.URL)
def create_block_url(block_id: int, url: schemas.URLCreate, db: Session = Depends(get_db)):
    return crud.create_url(db=db, url=url, building_block_id=block_id)
'''