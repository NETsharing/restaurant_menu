from fastapi import APIRouter

from app.api.menu import topping_api

router = APIRouter(prefix="/api/menu", responses={404: {"description": "Not found"}})

router.include_router(topping_api, prefix="/category", tags=["category"])
