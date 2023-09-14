from pydantic import BaseModel
from typing import Optional
from datetime import time

class GenerateSchedule(BaseModel):
    start_time: time
    end_time: time
    time_frame: time

class CreateAssignment(BaseModel):
    id_course: int
    year: int
    semester: int
    section: str
    assignment: int

class CreateCarrer(BaseModel):
    name: str

class CreateCourse(BaseModel):
    name: str
    semester: int
    carrer_id: int

class CreateTeacher(BaseModel):
    dpi: int
    name: str
    start_time: time
    end_time: time

class CreateClassroom(BaseModel):
    capacity: int
    name: str 

class CreateQualification(BaseModel):
    id_course: int
    dpi_teacher: int
    priority: int