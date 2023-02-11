from starlette import status
import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_category(async_client: AsyncClient):
    response = await async_client.post("/api/menu/category", json={})
    assert response.status_code == 200
    assert response.status_code == status.HTTP_200_OK
    for category in response.json():
        match category:
            case {'name': name}:
                assert name in ["Осеннее меню", "Летнее меню"]
        foods = category.get('foods')
        assert isinstance(foods, list)
        for food in foods:
            match food:
                case {'name': name}:
                    assert name in ["Смузи", "Кофе", "Чай"]


@pytest.mark.asyncio
@pytest.mark.parametrize("filter_key, value", [
    ("is_vegan", True),
])
async def test_is_vegan_filters(async_client: AsyncClient, filter_key: str, value: bool | str):
    body = {
        filter_key: value
    }

    response = await async_client.post("/api/menu/category", json=body)
    assert response.status_code == 200
    assert response.status_code == status.HTTP_200_OK

    for category in response.json():
        foods = category.get('foods')
        assert isinstance(foods, list)
        for food in foods:
            match food:
                case {'name': name}:
                    assert name in ["Смузи"]


@pytest.mark.asyncio
@pytest.mark.parametrize("filter_key, value", [
    ("is_vegan", False),
])
async def test_is_not_vegan_filters(async_client: AsyncClient, filter_key: str, value: bool | str):
    body = {
        filter_key: value
    }

    response = await async_client.post("/api/menu/category", json=body)
    assert response.status_code == 200
    assert response.status_code == status.HTTP_200_OK

    for category in response.json():
        foods = category.get('foods')
        assert isinstance(foods, list)
        for food in foods:
            match food:
                case {'name': name}:
                    assert name in ["Кофе", "Чай"]


@pytest.mark.asyncio
@pytest.mark.parametrize("filter_key, value", [
    ("is_special", True),
])
async def test_is_special_filters(async_client: AsyncClient, filter_key: str, value: bool | str):
    body = {
        filter_key: value
    }

    response = await async_client.post("/api/menu/category", json=body)
    assert response.status_code == 200
    assert response.status_code == status.HTTP_200_OK

    for category in response.json():
        foods = category.get('foods')
        assert isinstance(foods, list)
        for food in foods:
            match food:
                case {'name': name}:
                    assert name in ["Смузи", "Кофе", "Чай"]


@pytest.mark.asyncio
@pytest.mark.parametrize("filter_key, value", [
    ("is_special", False),
])
async def test_is_not_special_filters(async_client: AsyncClient, filter_key: str, value: bool | str):
    body = {
        filter_key: value
    }

    response = await async_client.post("/api/menu/category", json=body)
    assert response.status_code == 200
    assert response.status_code == status.HTTP_200_OK

    for category in response.json():
        foods = category.get('foods')
        assert isinstance(foods, list)
        for food in foods:
            match food:
                case {'name': name}:
                    assert name == []


@pytest.mark.asyncio
async def test_is_publish_filters(async_client: AsyncClient):

    response = await async_client.post("/api/menu/category", json={})
    assert response.status_code == 200
    assert response.status_code == status.HTTP_200_OK

    for category in response.json():
        foods = category.get('foods')
        assert isinstance(foods, list)
        for food in foods:
            match food:
                case {'name': name}:
                    assert name in ["Смузи", "Кофе", "Чай"]


@pytest.mark.asyncio
@pytest.mark.parametrize("filter_key, value", [
    ("topping_name", ["Корица", "Ваниль"]),
])
async def test_toppings_filters(async_client: AsyncClient, filter_key: str, value: bool | str):
    body = {
        filter_key: value
    }

    response = await async_client.post("/api/menu/category", json=body)
    assert response.status_code == 200
    assert response.status_code == status.HTTP_200_OK

    for category in response.json():
        foods = category.get('foods')
        for food in foods:
            toppings = food.get('toppings')
            assert isinstance(toppings, list)
            assert all(bool(z in value) for z in toppings)
