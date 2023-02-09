from sqlalchemy import (Column, String, Boolean, ForeignKey, Integer, PrimaryKeyConstraint)
from sqlalchemy.orm import relationship, relation

from app.models.base_model import Base, BaseModel


class Food(BaseModel):
    """  Блюдо """

    __tablename__ = 'food'
    __table_args__ = {"extend_existing": True}

    descriptions = Column(String)
    price = Column(Integer)
    is_special = Column(Boolean)
    is_vegan = Column(Boolean)
    is_publish = Column(Boolean)
    category_id = Column(Integer, ForeignKey('food_categories.id'), nullable=True)

    toppings = relationship('Topping', secondary='food_toppings', uselist=True)
    food_category = relationship('FoodCategory', back_populates='foods', uselist=False)


class Topping(BaseModel):
    """Ингредиенты"""

    __tablename__ = 'toppings'
    __table_args__ = {"extend_existing": True}


class FoodCategory(BaseModel):
    """Категория Блюд"""

    __tablename__ = 'food_categories'
    __table_args__ = {"extend_existing": True}

    is_publish = Column(Boolean)

    foods = relation('Food', uselist=True)


class FoodToppings(Base):
    """Категория Блюд"""

    __tablename__ = 'food_toppings'

    food_id = Column(Integer, ForeignKey('food.id'), nullable=False)
    topping_id = Column(Integer, ForeignKey('toppings.id'), nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint("food_id", "topping_id"),
        {},
    )
