from fastapi import FastAPI
from app.src.routes import api_router

app = FastAPI()
app.include_router(api_router)


@app.get('/')
def health_check():
    return {'message': 'ok'}
