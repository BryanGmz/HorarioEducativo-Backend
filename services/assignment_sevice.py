from sqlalchemy.orm import Session
from repositories import assignment, course
from objects.objects import AssignmentData
from schemas.schemas import CreateAssignment
from models.models import Assignment
from fastapi import HTTPException, status 

def get_assignments(db:Session):
    assignments = []
    for assigment in assignment.get_all_assignments(db):
        assignments.append(
            AssignmentData(
                id = assigment.id_assignment,
                assigned = assigment.assigned,
                carrer = assigment.carrer,
                course = assigment.course,
                section = assigment.section,
                year = assigment.year,
            )
        )
    return assignments

def create_assignment(assignment_data:CreateAssignment, db:Session):
    try:
        course_db = course.get_course_by_id(db, assignment_data.id_course)
        assignment_db = Assignment (
            course_id = assignment_data.id_course,
            carrer_id = course_db.carrer_id,
            year = assignment_data.year,
            semester = assignment_data.semester,
            section = assignment_data.section.upper(),
            assigned = assignment_data.assignment
        )
        assignment.create_assignment(assignment_db, db)
    except Exception as e :
        raise HTTPException (
            status_code = status.HTTP_409_CONFLICT,
            detail = f"Error creando la asignación {e}"
        )
    
def delete_assignment(id:int, db:Session):
    if (assignment.delete_assignment(id, db)):
        return {
            "response": "Asignación eliminada satisfactoriamente."
        }
    raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail=f"No existe la asignación con el id {id} por lo tanto no se elimina."
        )