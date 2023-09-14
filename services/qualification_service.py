from sqlalchemy.orm import Session
from repositories import qualification
from objects.objects import QualificationTeacherData
from schemas.schemas import CreateQualification
from models.models import Qualification
from fastapi import HTTPException, status

def get_qualification_by_dpi(dpi:int, db:Session):
    qualifications = []
    for _qualification in qualification.get_qualification_by_teacher_and_is_owner(db, dpi):
        qualifications.append(
            QualificationTeacherData(
                id = _qualification.id_qualification,
                course_id = _qualification.course_id,
                course_name = _qualification.course.name,
            )
        )
    return qualifications

def create_qualification(qualification_data:CreateQualification, db:Session):
    try:
        qualification_db = Qualification (
            teacher_dpi = qualification_data.dpi_teacher,
            course_id = qualification_data.id_course,
            is_owner = True if qualification_data.priority == 1 else False,
        )
        qualification.create_qualification(qualification_db, db)
    except Exception as e :
        raise HTTPException(
            status_code = status.HTTP_409_CONFLICT,
            detail = f"Error creando la cualificación {e}"
        )
    
def delete_qualification(id:int, db:Session):
    if (qualification.delete_qualification(id, db)):
        return {
            "response": "Cualificación eliminada satisfactoriamente."
        }
    raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail=f"No existe la cualificación con el id {id} por lo tanto no se elimina."
        )