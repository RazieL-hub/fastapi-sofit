import os
from typing import List
from fastapi import FastAPI, Query
from starlette.responses import JSONResponse

from apps.email.schemas import EmailSchema
from apps.email.send_email import send_email
from apps.telegram.send_message import send_message

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
    # await send_message(chat_id='-1001576623026', payload=f"{payload}")
    await send_email(EmailSchema(email=[os.getenv('MY_EMAIL')]), params={'title': 'REPORT', 'name': 'QWERTY'})
    return JSONResponse(status_code=200, content={"message": "email has been sent"})
