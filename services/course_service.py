from sqlalchemy.orm import Session
from repositories import course
from objects.objects import CourseData

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