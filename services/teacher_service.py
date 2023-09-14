from sqlalchemy.orm import Session
from repositories import teacher
from schemas.schemas import CreateTeacher
from models.models import Teacher
from fastapi import HTTPException, status

def get_teachers(db:Session):
    return teacher.get_all_teachers(db)

def create_teacher(teacher_data:CreateTeacher, db:Session):
    try:
        teacher_db = Teacher (
            dpi_teacher = teacher_data.dpi,
            name = teacher_data.name,
            start_conntracting_hour = teacher_data.start_time,
            end_conntracting_hour = teacher_data.end_time,
        )
        teacher.create_teacher(teacher_db, db)
    except Exception as e :
        raise HTTPException(
            status_code = status.HTTP_409_CONFLICT,
            detail = f"Error creando el profesor {e}"
        )
    
def delete_teacher(dpi:int, db:Session):
    if (teacher.delete_teacher(dpi, db)):
        return {
            "response": "Profesor eliminado satisfactoriamente."
        }
    raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail=f"No existe el profesor con el DPI {dpi} por lo tanto no se elimina."
        )