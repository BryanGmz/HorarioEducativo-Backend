from sqlalchemy.orm import Session
from repositories import course
from objects.objects import CourseData
from schemas.schemas import CreateCourse
from models.models import Course
from fastapi import HTTPException, status 

def get_courses(db:Session):
    courses = []
    for _course in course.get_all_courses(db):
        courses.append(CourseData(
            id = _course.id_course,
            carrer = _course.carrer,
            name = _course.name,
            semester = _course.semester,
            qualifications = [],
        )) 
    return courses

def create_course(course_data:CreateCourse, db:Session):
    try:
        course_db = Course (
            name = course_data.name,
            semester = course_data.semester,
            carrer_id = course_data.carrer_id,
        )
        course.create_course(course_db, db)
    except Exception as e :
        raise HTTPException(
            status_code = status.HTTP_409_CONFLICT,
            detail = f"Error creando el curso {e}"
        )
    
def delete_course(id:int, db:Session):
    if (course.delete_course(id, db)):
        return {
            "response": "Curso eliminado satisfactoriamente."
        }
    raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail=f"No existe curso con el id {id} por lo tanto no se elimina."
        )