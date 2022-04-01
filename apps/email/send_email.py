from fastapi_mail import MessageSchema, FastMail

from apps.email.schemas import EmailSchema
from core.settings import conf


async def send_email(email: EmailSchema, params: dict):
    body = f"""<html>
    <body style="margin: 0; padding: 0; box-sizing: border-box; font-family: Arial, Helvetica, sans-serif;">
    <div style="width: 100%; background: #efefef; border-radius: 10px; padding: 10px;">
        <div style="margin: 0 auto; width: 90%; text-align: center;">
            <h1 style="background-color: rgba(0, 53, 102, 1); padding: 5px 10px; border-radius: 5px; color: white;">{params['title']}</h1>
            <div style="margin: 30px auto; background: white; width: 40%; border-radius: 10px; padding: 50px; text-align: center;">
                <h3 style="margin-bottom: 100px; font-size: 24px;">{params['name']}!</h3>
                <p style="margin-bottom: 30px;">Lorem ipsum dolor sit amet consectetur adipisicing elit. Eligendi,
                    doloremque.</p>
                <a style="display: block; margin: 0 auto; border: none; background-color: rgba(255, 214, 10, 1); color: white; width: 200px; line-height: 24px; padding: 10px; font-size: 24px; border-radius: 10px; cursor: pointer; text-decoration: none;"
                   href="https://fastapi.tiangolo.com/"
                   target="_blank"
                >
                    Let's Go
                </a>
            </div>
        </div>
    </div>
    </body>
    </html>"""
    message = MessageSchema(
        subject="REPORT FROM SOFIT",
        recipients=email.dict().get("email"),  # List of recipients, as many as you can pass
        body=body,
        subtype="html"
    )
    fm = FastMail(conf)
    await fm.send_message(message)
