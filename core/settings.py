from pydantic_settings import BaseSettings
from pydantic import BaseModel


class RunConfig(BaseModel):
    port: int = 1234
    reload: bool = True


class Settings(BaseSettings):
    runCfg: RunConfig = RunConfig()
    
    
settings = Settings()