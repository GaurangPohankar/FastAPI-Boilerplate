from fastapi import FastAPI
from .models.common import run_migration
from .routers import blog, user,authentication

app = FastAPI()

run_migration()
    
app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)
