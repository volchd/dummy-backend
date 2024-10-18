from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app.db.database import Base
import enum

class StatusEnum(enum.Enum):
    NA = "NA"
    Defined = "Defined"
    Implementation_in_progress = "Implementation in progress"
    Implemented = "Implemented"

class ArchitectureLayer(Base):
    __tablename__ = "architecture_layers"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)
    
    building_blocks = relationship("ArchitectureBuildingBlock", back_populates="layer")
    urls = relationship("URL", back_populates="layer")

class ArchitectureBuildingBlock(Base):
    __tablename__ = "architecture_building_blocks"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String, unique=False, index=True)
    status = Column(Enum(StatusEnum), default=StatusEnum.NA)
    
    layer_id = Column(Integer, ForeignKey("architecture_layers.id"))
    layer = relationship("ArchitectureLayer", back_populates="building_blocks")
    
    urls = relationship("URL", back_populates="building_block")

class URL(Base):
    __tablename__ = "urls"
    
    id = Column(Integer, primary_key=True, index=True)
    url = Column(String)
    
    layer_id = Column(Integer, ForeignKey("architecture_layers.id"))
    layer = relationship("ArchitectureLayer", back_populates="urls")
    
    building_block_id = Column(Integer, ForeignKey("architecture_building_blocks.id"))
    building_block = relationship("ArchitectureBuildingBlock", back_populates="urls")
