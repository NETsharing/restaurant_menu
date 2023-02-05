from typing import List

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_async_session
from app.repositories.menu_repository import MenuRepository
from app.resources.filters import FILTER_CRITERIA_FOOD_MAP, FILTER_CRITERIA_TOPPING_MAP
from app.schemas.menu_schemas import MenuFilterParams, FoodCategorySchema


class MenuService:

    def __init__(self, db: AsyncSession = Depends(get_async_session)):
        self.repo = MenuRepository(db)

    async def get_dishes(self, filter_params: MenuFilterParams) -> List[FoodCategorySchema]:
        """" Возвращает блюда """

        food_filters, topping_filters = [], []

        if filter_params:
            for filter_model, value in filter_params.__dict__.items():
                if value is not None:
                    food = FILTER_CRITERIA_FOOD_MAP.get(filter_model)
                    if food:
                        food_filters.append(food(value))
                    topping = FILTER_CRITERIA_TOPPING_MAP.get(filter_model)
                    if topping and isinstance(value, list):
                        topping_filters.append(topping(value))

        food_filters.append(FILTER_CRITERIA_FOOD_MAP.get("is_publish")(True))
        return await self.repo.get_dishes(food_filters, topping_filters)
