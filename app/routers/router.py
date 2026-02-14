from fastapi import APIRouter
from routers.super_admin import routes as super_admin_routes

router = APIRouter(
    prefix="/api/v1",
)

router.include_router(super_admin_routes.router)