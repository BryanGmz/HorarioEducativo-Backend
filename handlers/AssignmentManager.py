from sqlalchemy.orm import Session
from repositories import assignment, course, qualification
from objects.objects import AssignmentData, CriterionData, Space, CourseData, CarrerData, TeacherData, ScheduleAssignmentData
from models.models import Teacher, Qualification

class AssignmentManager:
    
    def __init__(self, db:Session):
        self.db = db
        self.assignments = []

    def get_assigments_db(self):
        assignments_db = assignment.get_all_assignments(self.db)
        for assigment_db in assignments_db:
            qualifications_db = qualification.get_qualification_by_course(self.db, assigment_db.course_id)
            carrer_data = CarrerData (
                id = assigment_db.carrer.id_carrer,
                name = assigment_db.carrer.name)
            self.assignments.append(
                AssignmentData (
                    id = assigment_db.id_assignment,
                    carrer = carrer_data, 
                    course = CourseData (
                        id = assigment_db.course_id,
                        name = assigment_db.course.name,
                        semester = assigment_db.course.semester,
                        carrer = carrer_data,
                        qualifications = qualifications_db
                        ),
                    assigned = assigment_db.assigned,
                    section = assigment_db.section,
                    year = assigment_db.year))

    def add_warnings_unassigned(self, warning):
        for unassigned in self.get_unassigned():
            unassigned.warning = warning

    def get_unassigned(self):
        return list(filter(lambda assigment: not assigment.is_assigned, self.assignments))
    
    def filter_by_qualifications(self, teacher:Teacher):
        assignments = self.get_unassigned()
        filter_list = []
        courses = qualification.get_qualification_by_teacher_and_is_owner(self.db, teacher.dpi_teacher)
        for course in courses:
            for _assigment in assignments:
                if (course.course_id == _assigment.course.id): 
                    filter_list.append(_assigment)
        return filter_list
    
    def build_assignment(self, space:Space, assignment_data:AssignmentData, teacher:Teacher, priority, id:int):
        return ScheduleAssignmentData (
            classroom = space.classroom,
            year = assignment_data.year,
            course = assignment_data.course,
            semester = assignment_data.course.semester,
            start_time = space.start_time,
            end_time = space.end_time,
            section = assignment_data.section,
            teacher = TeacherData (
                dpi = teacher.dpi_teacher,
                name = teacher.name,
                start_conntracting_hour = teacher.start_conntracting_hour,
                end_conntraction_hour = teacher.end_conntracting_hour
            ),
            criterion = CriterionData(
                id = id,
                name =priority,),
            assigned = assignment_data.assigned,)  