from repositories import teacher
from handlers.ScheduleManager import ScheduleManager
from handlers.AssignmentManager import AssignmentManager
from sqlalchemy.orm import Session
from schemas.schemas import Period

class GenerateByHiringSchedule:
    
    def __init__(self, schedule_manager, assignment_manager, db:Session):
        self.schedule_manager:ScheduleManager = schedule_manager
        self.db = db

    def generate_schedule(self):
        periods = self.schedule_manager.get_periods()
        for period in periods:
            teachers_avaible = teacher.get_teacher_by_contracting_hour(self.db, period.start_time, period.end_time)
            if (teachers_avaible.count() > 0):
                for teacher_avaible in teachers_avaible:
                    