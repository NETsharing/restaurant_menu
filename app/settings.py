from enum import Enum, unique

from pydantic import PositiveInt
from pydantic.types import NonNegativeInt
from pydantic import BaseSettings as PyBaseSettings


@unique
class Environment(str, Enum):
    local = "local"
    development = "development"
    production = "production"


class BaseSettings(PyBaseSettings):
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


class ServerSettings(BaseSettings):
    server_host: str = "127.0.0.1"
    server_port: PositiveInt = 8015
    debug: bool = 0  # 1 to work with echo


class DatabaseSettings(BaseSettings):
    dialect: str = "postgresql"
    db_user: str = "postgres"
    db_pass: str = "postgres"
    db_host: str = "127.0.0.1"
    db_port: str = 5432
    db_name: str = "menu"

    db_pool_min_size: PositiveInt = 10
    db_pool_max_size: PositiveInt = 10
    statement_cache_size: NonNegativeInt = 0  # 0 to work with transaction_pooling

    @property
    def _uri(self):
        db_name = self.db_name
        return f"{self.db_user}:{self.db_pass}@{self.db_host}:{self.db_port}/{db_name}"

    @property
    def dsn_no_driver(self) -> str:
        return f"{self.dialect}://{self._uri}"

    @property
    def dsn(self) -> str:
        return f"{self.dialect}+asyncpg://{self._uri}"


db_settings = DatabaseSettings()
server_settings = ServerSettings()
