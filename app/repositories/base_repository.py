from abc import ABC, abstractmethod
from typing import Generic, Type, TypeVar

from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.base_schema import BaseSchema

SCHEMA = TypeVar("SCHEMA", bound=BaseSchema)
TABLE = TypeVar("TABLE")


class BaseRepository(Generic[SCHEMA, TABLE], ABC):
    def __init__(self, db: AsyncSession) -> None:
        self.db: AsyncSession = db

    @property
    @abstractmethod
    def _table(self) -> Type[TABLE]:
        pass

    @property
    @abstractmethod
    def _schema(self) -> Type[SCHEMA]:
        pass
