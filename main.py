import os

from fastapi import FastAPI

from core.settings import mail

app = FastAPI()


@app.get('/')
async def root():
    print(type(mail))
    print(mail)
    return {'message': mail}
