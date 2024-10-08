from .schemas import EmailCfgInSchema
from core.settings import settings



def send_mail(data: EmailCfgInSchema, smtp_server: str = settings.smtpCfg.server, smtp_port: int = settings.smtpCfg.port, password: str = settings.smtpCfg.password):
    pass