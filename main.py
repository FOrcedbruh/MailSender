from fastapi import FastAPI
import uvicorn
from core.settings import settings
from api import router

app = FastAPI()
app.include_router(router)

@app.get("/", response_model=dict)
def home() -> dict:
    return {
        "message": "Welcome to mail sender!"
    }



if __name__ == "__main__":
    uvicorn.run(app="main:app", port=settings.runCfg.port, reload=settings.runCfg.reload)