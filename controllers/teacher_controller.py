from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from config.database import get_db
from services.teacher_service import *

router = APIRouter (
    prefix = "/teacher",
    tags = ["Teacher"]
)

@router.get('/all/',status_code=status.HTTP_200_OK)
def hola(db:Session = Depends(get_db)):
    return {"teachers": get_teachers(db)}