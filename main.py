from typing import Union
from config.database import Base, engine, get_db
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from models.models import *
from handlers.ScheduleManager import ScheduleManager
from handlers.AssignmentManager import AssignmentManager
from generators.GenerateByHiringSchedule import GenerateByHiringSchedule 
from generators.GenerateByQualifications import GenerateByQualifications
from datetime import time
import uvicorn

def create_tables():
    Base.metadata.create_all(bind=engine)

create_tables()

app = FastAPI()

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)

@app.get("/")
def read_root(db:Session = Depends(get_db)):
    #data = db.query(Specialty).all()
    #print(data)
    
    schedule_manager = ScheduleManager(time(12, 0, 0,), time(21, 10, 0,), time(0, 50, 0,))
    assignment_manager = AssignmentManager(db)
    schedule_manager.generate_empty_schedule(db)
    assignment_manager.get_assigments_db()
    generate_by_hiring_schedule = GenerateByHiringSchedule(schedule_manager, assignment_manager, db)
    generate_by_qualifications = GenerateByQualifications(schedule_manager, assignment_manager, generate_by_hiring_schedule, db)
    #generate_by_hiring_schedule.generate_schedule()
    generate_by_qualifications.generate_schedule()
    print("----------------------------------------------------------------------------------------------------------------------------------")
    #print(schedule_manager.schedule)
    print("----------------------------------------------------------------------------------------------------------------------------------")
    print(assignment_manager.assignments)
    print("----------------------------------------------------------------------------------------------------------------------------------")
    
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}