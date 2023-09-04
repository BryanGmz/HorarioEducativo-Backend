from config.database import create_tables
from fastapi import FastAPI
from controllers import schedule_controller
import uvicorn

create_tables()

app = FastAPI()
app.include_router(schedule_controller.router)

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)