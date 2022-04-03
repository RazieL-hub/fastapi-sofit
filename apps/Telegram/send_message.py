import httpx
from starlette.responses import JSONResponse

from core.settings import BOT_TOKEN

token = BOT_TOKEN
api_telegram = f"https://api.telegram.org/bot{token}"
send_message_url = f"{api_telegram}/sendDocument"


async def send_report_to_telegram(chat_id: str, payload: str) -> JSONResponse:
    response = httpx.post(send_message_url, data={'chat_id': chat_id, 'document': payload})
    # return JSONResponse(status_code=200, content={"message": 'File send to telegram channel'})
