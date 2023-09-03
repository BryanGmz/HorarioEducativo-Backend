from sqlalchemy.orm import Session
from repositories import assignment, course
from schemas.schemas import AssignmentData, CriterionData, Space, CourseData, CarrerData, TeacherData, ScheduleAssignmentData, RequerimentData
from models.models import Teacher, Requirement
class AssignmentManager:
    
    def __init__(self, db:Session):
        self.db = db
        self.assignments = []

    def get_assigments_db(self):
        assignments_db = assignment.get_all_assignment(self.db)
        for assigment_db in assignments_db:
            requeriments_db = course.get_course_by_id(self.db, assigment_db.course_id).requeriments
            carrer_data = CarrerData (
                id = assigment_db.carrer.id_carrer,
                name = assigment_db.carrer.name)
            self.assignments.append(
                AssignmentData (
                    carrer = carrer_data, 
                    course = CourseData (
                        id = assigment_db.course_id,
                        name = assigment_db.course.name,
                        semester = assigment_db.course.semester,
                        carrer = carrer_data,
                        requeriments = self.add_requeriments(requeriments_db),
                    ),
                    assigned = assigment_db.assigned,
                    section = assigment_db.section,
                    year = assigment_db.year,
                    is_assigned=False))
    
    def add_requeriments(self, requeriments_db:Requirement):
        requeriments = []
        for requeriment_db in requeriments_db:
            requeriments.append(RequerimentData (
                area_id = requeriment_db.area_id,
                course_id = requeriment_db.course_id,
            ))
        return requeriments

    def add_warnings_unassigned(self, warning):
        for unassigned in self.get_unassigned():
            unassigned.warning = warning

    def get_unassigned(self):
        return list(filter(lambda assigment: not assigment.is_assigned, self.assignments))
    
    def check_contains_qualifications(self, teacher:Teacher, course:CourseData):
        for specialty in teacher.specialties:
            for requeriment in course.requeriments:
                if requeriment.area_id == specialty.area_id:
                    return True
        return False

    def filter_by_qualifications(self, teacher:Teacher):
        assignments = self.get_unassigned()
        print(len(assignments))
        filter_list = []
        for _assigment in assignments:
            if(self.check_contains_qualifications(teacher, _assigment.course)):
                filter_list.append(_assigment)
        return filter_list
    
    def build_assignment(self, space:Space, assignment_data:AssignmentData, teacher:Teacher, priority, id:int):
        return ScheduleAssignmentData (
            classroom = space.classroom,
            year = assignment_data.year,
            course = assignment_data.course,
            semester = assignment_data.course.semester,
            star_time = space.start_time,
            end_time = space.end_time,
            section = assignment_data.section,
            teacher = TeacherData (
                dpi = teacher.dpi_teacher,
                name = teacher.name,
                start_conntracting_hour = teacher.start_conntracting_hour,
                end_conntracting_hour = teacher.end_conntracting_hour,
            ),
            criterion = CriterionData(
                id = id,
                name =priority,)) 