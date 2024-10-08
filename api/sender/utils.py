from fastapi import Body
from .schemas import EmailCfgInSchema


def Send_mailForm(data: EmailCfgInSchema = Body()) -> EmailCfgInSchema:
    return EmailCfgInSchema(
        **data
    )