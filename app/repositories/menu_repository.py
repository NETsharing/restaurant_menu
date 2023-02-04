
from typing import Type, List

from pydantic import parse_obj_as, ValidationError
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from starlette.exceptions import HTTPException

from app.models import FoodCategory, Food
from app.repositories.base_repository import BaseRepository
from app.schemas.menu_schemas import FoodCategorySchema


class MenuRepository(BaseRepository):

    @property
    def _table(self) -> Type[FoodCategory]:
        return FoodCategory

    @property
    def _schema(self) -> Type[FoodCategorySchema]:
        return FoodCategorySchema

    async def get_dishes(self, food_filters: list, topping_filters: list) -> List[FoodCategorySchema]:
        """" Возвращает блюда """

        query = select(self._table).options(
            selectinload(self._table.foods.and_(*food_filters)).selectinload(Food.toppings.and_(*topping_filters)))

        result = await self.db.execute(query)

        try:
            return parse_obj_as(List[self._schema], result.scalars().all())
        except ValidationError as e:
            raise HTTPException(status_code=409, detail=f"{e}")
