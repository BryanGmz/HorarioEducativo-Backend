from sqlalchemy.orm import Session
from repositories import classroom
from schemas.schemas import CreateClassroom
from models.models import Classroom
from repositories import classroom
from fastapi import HTTPException, status

def get_classrooms(db:Session):
    return classroom.get_all_clasroom_asc(db)

def create_classroom(classroom_data:CreateClassroom, db:Session):
    try:
        classroom_db = Classroom (
            capacity = classroom_data.capacity,
            name = classroom_data.name,
        )
        classroom.create_clasroom(classroom_db, db)
    except Exception as e :
        raise HTTPException(
            status_code = status.HTTP_409_CONFLICT,
            detail = f"Error creando el salón {e}"
        )
    
def delete_classroom(id:int, db:Session):
    if (classroom.delete_classroom(id, db)):
        return {
            "response": "Salón eliminado satisfactoriamente."
        }
    raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail=f"No existe el salón con el id {id} por lo tanto no se elimina."
        )