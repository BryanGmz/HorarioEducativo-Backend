from config.database import create_tables
from fastapi import FastAPI
from controllers import schedule_controller
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

create_tables()

app = FastAPI()
app.include_router(schedule_controller.router)
origin = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origin,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
    )

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)