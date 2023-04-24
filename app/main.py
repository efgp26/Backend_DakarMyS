from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def home():
    return {"message": "Hello World, este es el Backend de la app Dakar"}