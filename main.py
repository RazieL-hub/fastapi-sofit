import os
from typing import List
from fastapi import FastAPI, Query, Request
from starlette.responses import JSONResponse

from apps.Telegram.send_message import send_report_to_telegram
from apps.email.schemas import EmailSchema
from apps.email.send_email import send_email

users = {
    1: {'first_name': 'test1', 'last_name': 'test1', 'how_send': 'email'},
    2: {'first_name': 'test2', 'last_name': 'test2', 'how_send': 'telegram'},
    3: {'first_name': 'test3', 'last_name': 'test3', 'how_send': 'email'},
    4: {'first_name': 'test4', 'last_name': 'test4', 'how_send': 'telegram'},
}

app = FastAPI()


@app.get('/')
async def root():
    return {'message': 'good'}


@app.post('/send-report')
async def send_report_asynchronous(
        type_event: str = Query(None, description='type_event'),
        users_id: List[str] = Query(None, description='Send report for users'),
        payload: str = Query(None, description='Link to file. This field required')) \
        -> JSONResponse:

    # await send_report_to_telegram(chat_id='-1001576623026', payload=f"{payload}")
    await send_email(EmailSchema(email=[os.getenv('MY_EMAIL')]), params={'title': 'REPORT', 'name': 'QWERTY'})
    return JSONResponse(status_code=200, content={"message": "email has been sent"})
