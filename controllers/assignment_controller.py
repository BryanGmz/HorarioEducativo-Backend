from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from config.database import get_db
from services.assignment_sevice import *

router = APIRouter (
    prefix = "/assignment",
    tags = ["Assigment"]
)

@router.get('/all/',status_code=status.HTTP_200_OK)
def hola(db:Session = Depends(get_db)):
    return {"assigments": get_assignments(db)}