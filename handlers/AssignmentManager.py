from sqlalchemy.orm import Session
from repositories import assignment, course, carrer
from schemas.schemas import AssignmentData, CourseData, CarrerData
from models.models import Carrer, Course, Assignment

class AssignmentManager:
    
    def __init__(self, db:Session):
        self.db = db
        self.assignments = []

    def get_assigments_db(self):
        assignments_db = assignment.get_all_assignment(self.db)
        for assigment_db in assignments_db:
            carrer_data = CarrerData (
                id = assigment_db.carrer.id_carrer,
                name = assigment_db.carrer.name)
            self.assignments.append(
                AssignmentData (
                    carrer = carrer_data, 
                    course = CourseData (
                        id = assigment_db.course.id_course,
                        name = assigment_db.course.name,
                        semester = assigment_db.course.semester,
                        carrer = carrer_data
                    ),
                    assigned = assigment_db.assigned,
                    section = assigment_db.section,
                    year = assigment_db.year,))
            
    def get_unassigned(self):
        return list(filter(lambda assigment: not assigment.is_assigned, self.assignments))