from fastapi import FastAPI
import logging

app = FastAPI()
logging.getLogger('api').setLevel(logging.CRITICAL)
# Import and include routers
from api.user import router as user_router
from api.budget import router as budget_router

app.include_router(user_router)
app.include_router(budget_router)