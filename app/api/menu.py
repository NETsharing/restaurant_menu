from typing import List

from fastapi import APIRouter, Depends, Body

from app.schemas.menu_schemas import MenuFilterParams, FoodCategorySchema
from app.services.menu_services import MenuService

topping_api = APIRouter()


@topping_api.post('', response_model=List[FoodCategorySchema])
async def get_dishes(filter_params: MenuFilterParams = Body(..., embed=False),
                     service: MenuService = Depends()):
    """" Возвращает блюда """

    return await service.get_dishes(filter_params)
