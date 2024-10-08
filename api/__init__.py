from fastapi import APIRouter
from .sender.views import router as senderRouter

router = APIRouter(prefix="/api")
router.include_router(router=senderRouter)
