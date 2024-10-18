
from fastapi import FastAPI

from .db.database import engine, Base

from .rest_api import api

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()
#add API router
app.include_router(api.router_layers)

'''
@app.post("/layers/", response_model=schemas.ArchitectureLayer)
def create_architecture_layer(layer: schemas.ArchitectureLayerCreate, db: Session = Depends(get_db)):
    return crud.create_architecture_layer(db=db, layer=layer)

@app.get("/layers/", response_model=List[schemas.ArchitectureLayer])
def read_architecture_layers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_architecture_layers(db=db, skip=skip, limit=limit)

@app.post("/layers/{layer_id}/blocks/", response_model=schemas.ArchitectureBuildingBlock)
def create_architecture_building_block(layer_id: int, block: schemas.ArchitectureBuildingBlockCreate, db: Session = Depends(get_db)):
    return crud.create_architecture_building_block(db=db, block=block, layer_id=layer_id)

@app.post("/layers/{layer_id}/urls/", response_model=schemas.URL)
def create_layer_url(layer_id: int, url: schemas.URLCreate, db: Session = Depends(get_db)):
    return crud.create_url(db=db, url=url, layer_id=layer_id)

@app.post("/blocks/{block_id}/urls/", response_model=schemas.URL)
def create_block_url(block_id: int, url: schemas.URLCreate, db: Session = Depends(get_db)):
    return crud.create_url(db=db, url=url, building_block_id=block_id)
'''