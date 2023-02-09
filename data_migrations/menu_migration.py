import asyncio
import random

from sqlalchemy import insert, select
from sqlalchemy.orm import selectinload

from app.database import async_session
from app.models.menu_models import Food, FoodCategory, Topping
from data_migrations.data.menu_data import food_categories, toppings, foods


async def create_test_data():
    """Creates test params"""

    async with async_session() as session:
        await session.execute(insert(FoodCategory).values(food_categories))
        await session.execute(insert(Food).values(foods))
        await session.execute(insert(Topping).values(toppings))
        await session.flush()
        food_category_entries = await session.execute(select(FoodCategory).options(selectinload(FoodCategory.foods)))
        food_entries = await session.execute(select(Food).options(selectinload(Food.toppings)))
        topping_entries = await session.execute(select(Topping))
        food_category_list = food_category_entries.scalars().all()
        food_list = food_entries.scalars().all()
        topping_list = topping_entries.scalars().all()
        for food_category in food_category_list:
            test_food_objs = random.sample(food_list, 2)
            for test_food_obj in test_food_objs:
                food_category.foods.append(test_food_obj)
                food_list.remove(test_food_obj)
                test_topping_objs = random.sample(topping_list, 2)
                test_food_obj.toppings.extend(test_topping_objs)
        await session.commit()


if __name__ == '__main__':
    asyncio.run(create_test_data())
