from sqlalchemy.orm import Session
from schemas.schemas import GenerateSchedule
from handlers.ScheduleManager import ScheduleManager
from handlers.AssignmentManager import AssignmentManager
from generators.GenerateByHiringSchedule import GenerateByHiringSchedule 
from generators.GenerateByQualifications import GenerateByQualifications
from generators.GenerateByAssignment import GenerateByAssignment
from objects.objects import ScheduleByPriority, Metric
from repositories import assignment, carrer, course, classroom, teacher

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
        unassigned = assignment_manager.get_unassigned(),
        metrics = [
            __get_metric_assignment__(assignment_manager),
            __get_metric_classroom__(db, schedule_manager),
            __get_metric_teacher__(db, schedule_manager),
        ]
    )

def __get_metric_assignment__(assignment_manager:AssignmentManager):
    avaible_value  = len(assignment_manager.get_unassigned())
    real_value = len(assignment_manager.assignments)
    return Metric (
        avaible_value = avaible_value,
        real_value = real_value,
        name = "Cursos",
    ) 

def __get_metric_classroom__(db:Session, schedule_manager:ScheduleManager):
    avaible_value  = schedule_manager.get_classroom_avaibles(db) 
    real_value = len(schedule_manager.get_by_period(0)) * len(schedule_manager.periods)
    return Metric (
        avaible_value = avaible_value,
        real_value = real_value,
        name = "Salones",
    ) 

def __get_metric_teacher__(db:Session, schedule_manager:ScheduleManager):
    real_value = len(teacher.get_all_teachers(db))
    avaible_value = real_value - schedule_manager.get_teachers_with_courses(db)
    return Metric (
        avaible_value = avaible_value,
        real_value = real_value,
        name = "Profesores",
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


def get_informative_data(db:Session):
    year = 2023
    return {
        "assigments": assignment.get_assigned_by_year(year, db),
        "carrers": len(carrer.get_all_carrers(db)),
        "courses": len(course.get_all_courses(db)),
        "classrooms": len(classroom.get_all_clasroom(db)),
        "teachers": len(teacher.get_all_teachers(db)),
    }