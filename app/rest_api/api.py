from typing import List
from fastapi import APIRouter, Depends,status
from sqlalchemy.orm import Session
from app.rest_api import schemas
from app.db import crud
from app.db.database import get_db


router_layers = APIRouter(
    prefix='/layers',
    tags=['Architecture Layers']
)

#create architecture layer
@router_layers.post("/", response_model=schemas.ArchitectureLayer)
def create_architecture_layer(layer: schemas.ArchitectureLayerCreate, db: Session = Depends(get_db)):
    return crud.create_architecture_layer(db=db, layer=layer)

#get all architecture layers
@router_layers.get("/", response_model=List[schemas.ArchitectureLayer])
def read_architecture_layers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_architecture_layers(db=db, skip=skip, limit=limit)

#get architecture layer
@router_layers.get("/{layer_id}", response_model=schemas.ArchitectureLayer)
def read_architecture_layer(layer_id: int, db: Session = Depends(get_db)):
    return crud.get_architecture_layer(db=db, layer_id=layer_id)

#update architecture layer
@router_layers.put("/{layer_id}", response_model=schemas.ArchitectureLayer)
def update_architecture_layers(layer_update: schemas.ArchitectureLayerCreate,layer_id: int, db: Session = Depends(get_db)):
    return crud.update_architecture_layer(db=db,layer_update=layer_update, layer_id=layer_id)

#delete architecture layer
@router_layers.delete("/{layer_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_architecture_layers(layer_id: int, db: Session = Depends(get_db)):
    crud.delete_architecture_layer(db=db, layer_id=layer_id)
    return {
        'msg': f'Architecture layer id:{layer_id} was deleted'
    } 
#create architecture building block
@router_layers.post("/{layer_id}/blocks/", response_model=schemas.ArchitectureBuildingBlock)
def create_architecture_building_block(layer_id: int, block: schemas.ArchitectureBuildingBlockCreate, db: Session = Depends(get_db)):
    return crud.create_architecture_building_block(db=db, block=block, layer_id=layer_id)

#get architecture building block
@router_layers.get("/{layer_id}/blocks/{block_id}", response_model=schemas.ArchitectureBuildingBlock)
def get_architecture_building_block(block_id: int, db: Session = Depends(get_db)):
    return crud.get_architecture_building_block(db=db,block_id=block_id)


# update architectute building block
@router_layers.put("/{layer_id}/blocks/{block_id}", response_model=schemas.ArchitectureBuildingBlock)
def update_architecture_building_block(block_id: int, block: schemas.ArchitectureBuildingBlockCreate, db: Session = Depends(get_db))->schemas.ArchitectureBuildingBlock:
    return crud.update_architecture_building_block(db=db, block=block, block_id=block_id)

#get all architecture building blocks for a architecture layer
@router_layers.get("/{layer_id}/blocks/", response_model=List[schemas.ArchitectureBuildingBlock])
def get_architecture_building_blocks(layer_id:int , db: Session = Depends(get_db))-> List[schemas.ArchitectureBuildingBlock]:
    return crud.get_all_architecture_building_block(db=db,layer_id=layer_id)

# update architectute building block
@router_layers.delete("/{layer_id}/blocks/{block_id}",  status_code=status.HTTP_204_NO_CONTENT)
def delete_architecture_building_block(layer_id: int,block_id: int, db: Session = Depends(get_db))->None:
    return crud.delete_architecture_building_block(db=db, layer_id=layer_id, block_id=block_id)


@router_layers.post("/{layer_id}/urls/", response_model=schemas.URL)
def create_layer_url(layer_id: int, url: schemas.URLCreate, db: Session = Depends(get_db)):
    return crud.create_url(db=db, url=url, layer_id=layer_id)

'''
@router_layers.post("/blocks/{block_id}/urls/", response_model=schemas.URL)
def create_block_url(block_id: int, url: schemas.URLCreate, db: Session = Depends(get_db)):
    return crud.create_url(db=db, url=url, building_block_id=block_id)
'''