from fastapi import APIRouter
from .breed import router as breed

router = APIRouter()
router.include_router(breed)