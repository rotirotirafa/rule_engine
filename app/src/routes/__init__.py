from fastapi import APIRouter

from app.src.routes.rules import RulesRoute

api_router = APIRouter()

api_router.include_router(RulesRoute, tags=['Rules-Regras'])
