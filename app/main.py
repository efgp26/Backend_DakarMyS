from fastapi import FastAPI

from app.router.user_router import router as user_router
from app.router.rol_router import router as rol_router

app = FastAPI()

app.include_router(user_router)
app.include_router(rol_router)

@app.get('/')
def home():
    return {"message": "Hello World, este es el Backend de la app Dakar"}