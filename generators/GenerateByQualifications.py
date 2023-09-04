from sqlalchemy.orm import Session
from handlers.ScheduleManager import ScheduleManager
from handlers.AssignmentManager import AssignmentManager
from generators.GenerateByHiringSchedule import GenerateByHiringSchedule
from repositories import teacher
from objects.objects import Space

class GenerateByQualifications:
    
    def __init__(self, schedule_manager, assignment_manager, generate_by_hiring_schedule, db:Session):
        self.schedule_manager:ScheduleManager = schedule_manager
        self.assignment_manager:AssignmentManager = assignment_manager
        self.generate_by_hiring_schedule:GenerateByHiringSchedule = generate_by_hiring_schedule
        self.db = db

    def get_periods_by_contracting_hour(self, start_time, end_time):
        filter_periods = []
        for period in self.schedule_manager.get_periods():
            if (period.start_time >= start_time and period.end_time <= end_time):
                filter_periods.append(period)
        return filter_periods

    def generate_schedule(self):
        teachers = teacher.get_all_teacher(self.db)
        for teacher_db in teachers:
            courses = self.assignment_manager.filter_by_qualifications(teacher_db)
            if (len(courses) > 0):
                periods = self.get_periods_by_contracting_hour(teacher_db.start_conntracting_hour, teacher_db.end_conntracting_hour)
                for course in courses:
                    if(len(periods) > 0):
                        for period in periods:
                            space:Space = self.generate_by_hiring_schedule.verify_space_by_capaciy(period.index, course.assigned)
                            if (space != None):
                                course.is_assigned = True
                                space.schedule_assignment = self.assignment_manager.build_assignment(space, course, teacher_db, 'Por Cualificaciones', 2)
                            else:
                                course.warning = "No asignado debido a que no se encontro salón con la capacidad necesaria."
                    else:
                        course.warning = "No asignado debido a que no hay profesores disponibles por el horario de contratación."
        self.assignment_manager.add_warnings_unassigned("No asignado debido a que no hay profesores con las cualificaciones requeridas por el curso.")
                    
                        
                    
