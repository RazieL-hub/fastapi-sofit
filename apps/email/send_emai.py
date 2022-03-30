from fastapi_mail import ConnectionConfig

from core.settings import MAIL_SERVER, MAIL_PASSWORD, MAIL_PORT, MAIL_FROM_NAME

conf = ConnectionConfig(
    MAIL_USERNAME=MAIL_SERVER,
    MAIL_PASSWORD=MAIL_PASSWORD,
    MAIL_PORT=MAIL_PORT,
    MAIL_SERVER=MAIL_SERVER,
    MAIL_FROM_NAME=MAIL_FROM_NAME,
    MAIL_TLS=True,
    MAIL_SSL=False,
    USE_CREDENTIALS=True,
    TEMPLATE_FOLDER='apps/email/templates/email'
)
