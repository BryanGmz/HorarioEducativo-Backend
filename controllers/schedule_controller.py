from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from config.database import get_db
from services import schedule_service
from schemas.schemas import GenerateSchedule

router = APIRouter (
    prefix = "/schedule",
    tags = ["Schedule"]
)

@router.get('/',status_code=status.HTTP_200_OK)
def hola(db:Session = Depends(get_db)):
    return {"Hola": "Hola"}

@router.post('/',status_code=status.HTTP_200_OK)
def generate_schedule(generate_schedule:GenerateSchedule,  db:Session = Depends(get_db)):
    return schedule_service.get_schedule(db, generate_schedule)