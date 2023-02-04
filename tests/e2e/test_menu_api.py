from starlette import status
import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_menu_category(async_client: AsyncClient):
    body = {
        "is_vegan": True,
    }
    response = await async_client.post("/api/menu/category", json=body)
    assert response.status_code == 200
    assert response.status_code == status.HTTP_200_OK
