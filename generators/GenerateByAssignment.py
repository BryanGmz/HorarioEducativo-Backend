from sqlalchemy.orm import Session
from handlers.AssignmentManager import AssignmentManager
from handlers.ScheduleManager import ScheduleManager
from generators.GenerateByHiringSchedule import GenerateByHiringSchedule
from repositories import teacher, qualification
from objects.objects import AssignmentData

class GenerateByAssignment:

    def __init__(self, schedule_manager, assignment_manager, generate_by_hiring_schedule, db:Session):
        self.schedule_manager:ScheduleManager = schedule_manager
        self.assignment_manager:AssignmentManager = assignment_manager
        self.generate_by_hiring_schedule:GenerateByHiringSchedule = generate_by_hiring_schedule
        self.db = db

    def verify_teacher_avaible_schedule(self, period):
        teachers_avaible = teacher.get_teacher_by_contracting_hour(self.db, period.start_time, period.end_time)
        classrooms_assigned = self.schedule_manager.get_classroom_assinged(period.index)
        teacher_avaible_in_the_period = []
        for teacher_avaible in teachers_avaible:
            flag_assignado = False
            for clasroom_assigned in classrooms_assigned:
                if (clasroom_assigned.schedule_assignment.teacher.dpi == teacher_avaible.dpi_teacher):
                    flag_assignado = True
                    break
            if (not flag_assignado):
                teacher_avaible_in_the_period.append(teacher_avaible)
        return teacher_avaible_in_the_period

    def get_qualificated_teacher(self, teachers, assigment:AssignmentData):
        for teacher in teachers:
            if(qualification.get_qualification_by_composite_key(self.db, assigment.course.id, teacher.dpi_teacher) != None):
                return teacher
        return None

    def generate_schedule(self):
        unassigneds = self.assignment_manager.get_unassigned()
        periods = self.schedule_manager.get_periods()
        for unassigned in unassigneds:
            for period in periods:
                if (not unassigned.is_assigned):
                    classroom = self.generate_by_hiring_schedule.verify_space_by_capaciy(period.index, unassigned.assigned)
                    if (classroom != None):
                        teachers_avaible = self.verify_teacher_avaible_schedule(period)
                        if (len(teachers_avaible) > 0):
                            qualificated_teacher = self.get_qualificated_teacher(teachers_avaible, unassigned)  
                            if(qualificated_teacher != None):
                                unassigned.is_assigned = True
                                classroom.schedule_assignment = self.assignment_manager.build_assignment(classroom, unassigned, qualificated_teacher, 'Por Asignación de Cursos y Espacios', 3)
                            else:
                                unassigned.warning = "Sin asignar debido a que no hay profesores con las cualificaciones requeridas por el curso en los periodos disponibles."
                        else: 
                            unassigned.warning = "Sin asignar debido a la falta de disponibilidad de profesores en los periodos disponibles, a causa del horario de contratación."
                    else: 
                        unassigned.warning = "Sin asignar debido a que no se encontro salón con la capacidad necesaria en los periodos disponibles."