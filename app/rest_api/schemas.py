from typing import List
from enum import Enum
from pydantic import BaseModel

class StatusEnum(str, Enum):
    NA = "NA"
    Defined = "Defined"
    Implementation_in_progress = "Implementation in progress"
    Implemented = "Implemented"

class URLBase(BaseModel):
    url: str

class URLCreate(URLBase):
    pass

class URL(URLBase):
    id: int

    class Config:
        orm_mode = True

class ArchitectureBuildingBlockBase(BaseModel):
    name: str
    description: str
    status: StatusEnum

class ArchitectureBuildingBlockCreate(ArchitectureBuildingBlockBase):
    pass

class ArchitectureBuildingBlock(ArchitectureBuildingBlockBase):
    id: int
    layer_id: int
    urls: List[URL] = []

    class Config:
        orm_mode = True

class ArchitectureLayerBase(BaseModel):
    name: str
    description: str

class ArchitectureLayerCreate(ArchitectureLayerBase):
    pass

class ArchitectureLayer(ArchitectureLayerBase):
    id: int
    building_blocks: List[ArchitectureBuildingBlock] = []
    urls: List[URL] = []

    class Config:
        orm_mode = True
