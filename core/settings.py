from pydantic_settings import BaseSettings
from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

SMTP_PORT: str = os.environ.get("SMTP_PORT")
SMTP_SERVER: str = os.environ.get("SMTP_SERVER")
PASS: str = os.environ.get("PASS")

class SMTPConfig(BaseModel):
    server: str = SMTP_PORT
    port: int = SMTP_PORT
    password: str = PASS

class RunConfig(BaseModel):
    port: int = 1234
    reload: bool = True


class Settings(BaseSettings):
    runCfg: RunConfig = RunConfig()
    smtpCfg: SMTPConfig = SMTPConfig()
    
    
settings = Settings()