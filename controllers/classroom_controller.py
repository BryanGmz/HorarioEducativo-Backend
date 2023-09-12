from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from config.database import get_db
from services.classrooms_service import *

router = APIRouter (
    prefix = "/classroom",
    tags = ["Classroom"]
)

@router.get('/all/',status_code=status.HTTP_200_OK)
def hola(db:Session = Depends(get_db)):
    return {"classrooms": get_classrooms(db)}