from fastapi_mail import ConnectionConfig, MessageSchema, FastMail

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


async def send_email_async(subject: str, email_to: str, body: dict):
    message = MessageSchema(
        subject=subject,
        recipients=[email_to],
        body=body,
        subtype='html',
    )

    fm = FastMail(conf)
    await fm.send_message(message, template_name='email.html')
