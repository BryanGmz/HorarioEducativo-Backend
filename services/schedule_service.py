from sqlalchemy.orm import Session
from schemas.schemas import GenerateSchedule
from handlers.ScheduleManager import ScheduleManager
from handlers.AssignmentManager import AssignmentManager
from generators.GenerateByHiringSchedule import GenerateByHiringSchedule 
from generators.GenerateByQualifications import GenerateByQualifications
from generators.GenerateByAssignment import GenerateByAssignment
from datetime import time
from objects.objects import ScheduleByPriority

def __create_schedule_manager__(generate_schedule:GenerateSchedule, db:Session):
    schedule_manager = ScheduleManager (
        start_time = generate_schedule.start_time,
        end_time = generate_schedule.end_time,
        time_frame = generate_schedule.time_frame
    )
    schedule_manager.generate_empty_schedule(db)
    return schedule_manager

def __create_assignment_manager__(db:Session):
    assignment_manager = AssignmentManager(db)
    assignment_manager.get_assigments_db()
    return assignment_manager

def __get_schedule_by_priorities__(schedule_manager:ScheduleManager, assignment_manager:AssignmentManager, priority:int, db:Session):
    generate_by_hiring_schedule = GenerateByHiringSchedule(schedule_manager, assignment_manager, db)
    if (priority == 1): # By Assignment
        generate_by_assignment = GenerateByAssignment(schedule_manager, assignment_manager, generate_by_hiring_schedule, db)
        generate_by_assignment.generate_schedule()
        schedule_manager.sort_classrooms()
    elif (priority == 2): # By Hiring Schedule
        generate_by_hiring_schedule.generate_schedule()
        schedule_manager.sort_classrooms()
    else: # By Qualifications
        generate_by_qualifications = GenerateByQualifications(schedule_manager, assignment_manager, generate_by_hiring_schedule, db)
        generate_by_qualifications.generate_schedule()
        schedule_manager.sort_classrooms()
    return ScheduleByPriority (
        schedule = schedule_manager.schedule,
        unassigned = assignment_manager.get_unassigned()
    )

def get_schedule(db:Session, generate_schedule:GenerateSchedule):
    schedule_manager = __create_schedule_manager__(generate_schedule, db)
    assignment_manager = __create_assignment_manager__(db)
    schedule_by_priorities = [
        __get_schedule_by_priorities__(schedule_manager, assignment_manager, 1, db),
        __get_schedule_by_priorities__(__create_schedule_manager__(generate_schedule, db), __create_assignment_manager__(db), 2, db),
        __get_schedule_by_priorities__(__create_schedule_manager__(generate_schedule, db), __create_assignment_manager__(db), 3, db)
    ]
    return {
        "schedule_by_priorities" : schedule_by_priorities,
        "periods" : schedule_manager.periods,
        "time_information" : generate_schedule,
        "classrooms" : schedule_manager.get_by_period(0)
    }
