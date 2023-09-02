from pydantic import BaseModel
from datetime import time
from typing import List

class CarrerData(BaseModel):
    id: int
    name: str

class CourseData(BaseModel):
    id: int
    name: str
    semester: int
    carrer: CarrerData
    requeriments: List[]

class AssignmentData(BaseModel):
    course: CourseData
    carrer: CarrerData
    year: int
    section: str
    assigned: int
    is_assigned: bool = False

class AreaData(BaseModel):
    id: int
    name: str
    
class SpecialtyData(BaseModel):
    area: AreaData
    teacher_dpi: int

class TeacherData(BaseModel):
    dpi: int
    name: str
    start_conntracting_hour: time 
    end_conntracting_hour: time
    specialties: List[SpecialtyData] = []

class ClassroomData(BaseModel):
    id: int
    name: str
    capacity: int

class RequerimentData(BaseModel):
    area: AreaData
    course_id: int

class CriterionData(BaseModel):
    id: int
    name: str

class ScheduleAssignmentData(BaseModel):
    course: CourseData
    classroom: ClassroomData
    teacher: TeacherData
    criterion:  CriterionData
    section: str
    year: int
    semester: int
    star_time: time
    end_time: time
    warnings: list[str] = []

class Space(BaseModel):
    classroom: ClassroomData
    start_time: time
    end_time: time
    i_index: int
    j_index: int
    schedule_assignment: ScheduleAssignmentData = None

class Period (BaseModel):
    start_time: time
    end_time: time
    index: int