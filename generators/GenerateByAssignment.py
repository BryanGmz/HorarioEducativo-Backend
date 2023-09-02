from repositories import assignment, course, carrer
from models.models import Assignment, Course, Carrer
from schemas.schemas import *

class GenerateByAssignment:

    def __init__(self, schedule, unssigned_list):
        self.schedule = schedule
        self.unssigned_list = unssigned_list

    def check_capacity_for_allocation(self, course:Assignment, space:Space):
        return course.assigned <= space.classroom.capacity
            
"""
    def build_assigment(schedule_assignment:Assignment, classrom:ClassroomData):
        course_db:Course = course.get_course_by_id(schedule_assignment.course_id)
        carrrer_db:Carrer = carrer.get_carrer_by_id(course_db.carrer_id)
        return ScheduleAssignmentData(
            classroom=classrom,
            year=schedule_assignment.year,
            course=CourseData(
                id=course_db.id_course,
                carrer=CarrerData(
                    id=carrrer_db.id_carrer,
                    name=carrrer_db.name,
                ),
                name=course_db.name,
                semester=schedule_assignment.semester  
            ),
            semester=schedule_assignment.semester,
            star_time=schedule_assignment
        )
"""

   