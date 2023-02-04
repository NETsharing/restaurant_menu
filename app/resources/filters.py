from app.models import Food, Topping

FILTER_CRITERIA_FOOD_MAP = {
    'is_vegan': Food.is_vegan.is_,
    'is_special': Food.is_special.is_,
    'is_publish': Food.is_publish.is_
}

FILTER_CRITERIA_TOPPING_MAP = {
    'topping_name': Topping.name.in_,
}
