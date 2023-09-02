from typing import Union
from config.database import Base, engine, get_db
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from models.models import *
from handlers.ScheduleManager import ScheduleManager
from datetime import time
import uvicorn

def create_tables():
    Base.metadata.create_all(bind=engine)

create_tables()

schedule_manager = ScheduleManager(time(12, 0, 0,), time(21, 10, 0,), time(0, 50, 0,))
app = FastAPI()

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)

@app.get("/")
def read_root(db:Session = Depends(get_db)):
    data = db.query(Specialty).all()
    
    print(schedule_manager.generate_empty_schedule(db))
    print(schedule_manager.get_classroom_by_capacity_desc(db, 0))
    print(schedule_manager.get_periods())
    print(data[0].area.name)
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}