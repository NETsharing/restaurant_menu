import asyncio
from typing import Generator

import pytest
import pytest_asyncio
from httpx import AsyncClient

from app.database import _get_engine
from app.instances import app
from app.settings import db_settings

async_engine = _get_engine(db_settings)


@pytest.fixture(scope="session")
def event_loop(request) -> Generator:
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture(scope='session')
async def async_client():
    async with AsyncClient(app=app, base_url="http://127.0.0.1:8015") as client:
        yield client
