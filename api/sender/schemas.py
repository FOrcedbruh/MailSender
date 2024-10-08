from pydantic import BaseModel


class EmailCfgInSchema(BaseModel):
    sender_email: str
    recipient_email: str
    subject: str
    body: str