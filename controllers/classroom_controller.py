from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from config.database import get_db
from services import classrooms_service
from schemas.schemas import CreateClassroom

router = APIRouter (
    prefix = "/classroom",
    tags = ["Classroom"]
)

@router.get('/all/',status_code=status.HTTP_200_OK)
def get_classrooms(db:Session = Depends(get_db)):
    return {"classrooms": classrooms_service.get_classrooms(db)}

@router.post('/', status_code = status.HTTP_201_CREATED)
def create_classroom(classroom_data:CreateClassroom, db:Session = Depends(get_db)):
    classrooms_service.create_classroom(classroom_data, db)
    return {
        "response": "Salón creado satisfactoriamente."
    }

@router.delete('/{id}', status_code = status.HTTP_200_OK)
def delete_classroom(id:int, db:Session = Depends(get_db)):
    return classrooms_service.delete_classroom(id, db)