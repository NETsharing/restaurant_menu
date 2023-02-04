from sqlalchemy import (Column, Integer, String)
from sqlalchemy.orm import registry

mapper_registry = registry()
Base = mapper_registry.generate_base()


class BaseModel(Base):
    __abstract__ = True

    id = Column(Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)
