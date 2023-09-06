from repositories import teacher
from handlers.ScheduleManager import ScheduleManager
from handlers.AssignmentManager import AssignmentManager
from sqlalchemy.orm import Session
from objects.objects import Space

class GenerateByHiringSchedule:
    
    def __init__(self, schedule_manager, assignment_manager, db:Session):
        self.schedule_manager:ScheduleManager = schedule_manager
        self.assignment_manager:AssignmentManager = assignment_manager
        self.db = db

    def verify_space_by_capaciy(self, period, necessary_capacity:int):
        spaces = self.schedule_manager.get_classroom_by_capacity_desc(self.db, period)
        if (len(spaces) > 0):
            for space in spaces:
                if (space.classroom.capacity >= necessary_capacity):
                    return space  
        return None

    def generate_schedule(self):
        periods = self.schedule_manager.get_periods()
        for period in periods:
            teachers_avaible = teacher.get_teacher_by_contracting_hour(self.db, period.start_time, period.end_time)
            if (len(teachers_avaible) > 0):
                for teacher_avaible in teachers_avaible:
                    courses = self.assignment_manager.filter_by_qualifications(teacher_avaible)
                    if (len(courses) > 0):
                        for course in courses:
                            space:Space = self.verify_space_by_capaciy(period.index, course.assigned)
                            if (space != None):
                                course.is_assigned = True
                                space.schedule_assignment = self.assignment_manager.build_assignment(space, course, teacher_avaible, 'Por Horario de Contratación', 1)
                                break
                            else:
                                course.warning = "No asignado debido a que no se encontro salón con la capacidad necesaria."
            else:
                self.assignment_manager.add_warnings_unassigned("No asignado debido a que no hay profesores con las cualificaciones requeridas por el curso.")
        self.assignment_manager.add_warnings_unassigned("No asignado debido a que no hay profesores disponibles por el horario de contratación.")