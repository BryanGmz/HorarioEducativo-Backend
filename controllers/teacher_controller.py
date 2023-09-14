from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from config.database import get_db
from services import teacher_service
from schemas.schemas import CreateTeacher

router = APIRouter (
    prefix = "/teacher",
    tags = ["Teacher"]
)

@router.get('/all/',status_code=status.HTTP_200_OK)
def get_teachers(db:Session = Depends(get_db)):
    return {"teachers": teacher_service.get_teachers(db)}

@router.post('/', status_code = status.HTTP_201_CREATED)
def create_teacher(teacher_data:CreateTeacher, db:Session = Depends(get_db)):
    teacher_service.create_teacher(teacher_data, db)
    return {
        "response": "Profesor creado satisfactoriamente."
    }

@router.delete('/{dpi}', status_code = status.HTTP_200_OK)
def delete_teacher(dpi:int, db:Session = Depends(get_db)):
    return teacher_service.delete_teacher(dpi, db)