from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from config.database import get_db
from services import course_service
from schemas.schemas import CreateCourse

router = APIRouter (
    prefix = "/course",
    tags = ["Course"]
)

@router.get('/all/',status_code=status.HTTP_200_OK)
def get_courses(db:Session = Depends(get_db)):
    return {"courses": course_service.get_courses(db)}

@router.post('/', status_code = status.HTTP_201_CREATED)
def create_course(course_data:CreateCourse, db:Session = Depends(get_db)):
    course_service.create_course(course_data, db)
    return {
        "response": "Curso creado satisfactoriamente."
    }

@router.delete('/{id}', status_code = status.HTTP_200_OK)
def delete_course(id:int, db:Session = Depends(get_db)):
    return course_service.delete_course(id, db)