from datetime import time
from typing import List

class CarrerData:

    def __init__(self, id = int, name = str):
        self.id = id
        self.name = name

class CourseData:
        
    def __init__(self, id:int, name:str, semester:int, carrer:CarrerData, qualifications):
        self.id = id
        self.name = name
        self.semester = semester
        self.carrer:CarrerData = carrer
        self.qualifications = qualifications

class AssignmentData:
        
    def __init__(self, course:CourseData, carrer:CarrerData, year:int, section:str, assigned:int):
        self.course:CourseData = course
        self.carrer:CarrerData = carrer
        self.year = year
        self.section = section
        self.assigned = assigned
        self.is_assigned = False
        self.warning = None

class TeacherData:
    
    def __init__(self, dpi:int, name:str, start_conntracting_hour:time, end_conntraction_hour:time):
        self.dpi = dpi
        self.name = name
        self.start_conntracting_hour = start_conntracting_hour
        self.end_conntraction_hour = end_conntraction_hour
        self.qualifications = []

class ClassroomData:
    
    def __init__(self, id:int, name:str, capacity:int):
        self.id = id
        self.name = name
        self.capacity = capacity

class CriterionData:
    
    def __init__(self, id:int, name:str):
        self.id = id
        self.name = name

class ScheduleAssignmentData:
        
    def __init__(self, course:CourseData, classroom:ClassroomData, teacher:TeacherData, criterion:CriterionData, section:str, year:str, semester:int, start_time:time, end_time:time, assigned:int):
        self.course:CourseData = course
        self.classroom:ClassroomData = classroom
        self.teacher:TeacherData = teacher
        self.criterion:CriterionData =  criterion
        self.section = section
        self.year = year
        self.semester = semester
        self.star_time = start_time
        self.end_time = end_time
        self.warnings = None
        self.assigned = assigned

class Space:
        
    def __init__(self, classroom:ClassroomData, start_time:time, end_time:time, i_index:int, j_index):
        self.classroom:ClassroomData = classroom 
        self.start_time = start_time
        self.end_time = end_time
        self.i_index = i_index
        self.j_index = j_index
        self.schedule_assignment:ScheduleAssignmentData = None

class Period:
    
    def __init__(self, start_time:time, end_time:time, index:int):
        self.start_time = start_time
        self.end_time = end_time
        self.index = index

class ScheduleByPriority:

    def __init__(self, schedule, unassigned):
        self.schedule = schedule # Matriz creada para almacenar el horario en donde las filas son los periodos y columnas son salones
        self.unassigned = unassigned # Listado de cursos si ser asignados

class QualificationData:
    
    def __init__(self, dpi_teacher, course_id, is_owner) -> None:
        self.dpi_teacher = dpi_teacher
        self.course_id = course_id
        self.is_owner = is_owner
    