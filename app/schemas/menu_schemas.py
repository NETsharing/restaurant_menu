from typing import List

from pydantic import root_validator

from app.schemas.base_schema import BaseSchema


class ToppingSchema(BaseSchema):
    """Ингредиенты"""

    name: str

    class Config:
        orm_mode = True


class FoodSchema(BaseSchema):
    """  Блюдо """

    name: str
    descriptions: str
    price: int
    is_special: bool
    is_vegan: bool

    toppings: list

    @root_validator
    def mainroot(cls, values):
        toppings = values.get('toppings')
        if toppings and not isinstance(toppings[0], str):
            values["toppings"] = [topping.name for topping in toppings]
        return values

    class Config:
        orm_mode = True


class FoodCategorySchema(BaseSchema):
    """Категория Блюд"""

    id: int
    name: str

    foods: List[FoodSchema]

    class Config:
        orm_mode = True


class MenuFilterParams(BaseSchema):
    """Фильтр Блюд"""

    is_vegan: bool | None = None
    is_special: bool | None = None
    topping_name: List[str] | None = None
