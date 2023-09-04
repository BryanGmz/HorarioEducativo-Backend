from datetime import time, timedelta
from math import ceil
from objects.objects import Space, ClassroomData, Period
from repositories.classroom import *
from models.models import Classroom

class ScheduleManager:

    def __init__(self, start_time:time, end_time:time, time_frame:time):
        self.start_time = start_time
        self.end_time = end_time
        self.time_frame = time_frame
        self.start_time_td = timedelta(hours=start_time.hour, minutes=self.start_time.minute, seconds=self.start_time.second)
        self.end_time_td = timedelta(hours=end_time.hour, minutes=end_time.minute, seconds=end_time.second)
        self.time_frame_td = timedelta(hours=time_frame.hour, minutes=time_frame.minute, seconds=time_frame.second)
        self.schedule = None
        self.periods = []
        self.len_classrooms = 0
        self.len_periods = 0
        
    def build_classroom(classroom:Classroom):
        return ClassroomData(
            id = classroom.id_classroom,
            capacity = classroom.capacity,
            name = classroom.name,
        )
    
    def parse_time(self, time_delta:timedelta):
        return time(
            hour = int(time_delta.seconds / 3600),
            minute = int((time_delta.seconds % 3600) / 60),
            second = int(time_delta.seconds % 60))

    def generate_new_hour(self, iteration:int):
        new_time = (self.time_frame_td * iteration) + self.start_time_td
        return self.parse_time(new_time)

    def generate_end_time(self, start_time_assigned:time):
        return self.parse_time(
            timedelta(
                hours=start_time_assigned.hour, 
                minutes=start_time_assigned.minute, 
                seconds=start_time_assigned.second) + self.time_frame_td)

    def get_len_periods(self):
        return ceil((self.end_time_td - self.start_time_td)/self.time_frame_td)
    
    def generate_empty_schedule(self, db:Session):
        classrooms = get_all_clasroom(db)
        self.len_periods = self.get_len_periods()
        self.len_periods = self.len_periods if self.len_periods > 0 else self.len_periods - 1
        self.len_classrooms = len(classrooms)
        self.schedule = [[None for _ in range(len(classrooms))] for _ in range(self.len_periods)]
        for i in range(self.len_periods):
            start_hour:time = self.generate_new_hour(i + 1)
            for j in range(len(classrooms)):
                self.schedule[i][j] = Space(
                    classroom = ClassroomData(
                        id = classrooms[j].id_classroom,
                        capacity = classrooms[j].capacity,
                        name = classrooms[j].name,
                    ),
                    start_time = start_hour,
                    end_time = self.generate_end_time(start_hour),
                    i_index = i,
                    j_index = j,
                )
            self.periods.append(Period(
                start_time = start_hour,
                end_time = self.generate_end_time(start_hour),
                index = i 
            ))
    
    def get_periods(self):
        return self.periods

    def get_by_period(self, period:int):
        return self.schedule[period]

    def sort_classrom_space(self, spaces):
        return sorted(spaces, key = lambda space : space.classroom.capacity, reverse = True)

    def get_classroom_assinged(self, period):
        sorted_classroom = self.sort_classrom_space(self.get_by_period(period))
        classrooms = []
        for space in sorted_classroom:
            if (space.schedule_assignment != None):
                classrooms.append(space)
        return classrooms

    def get_classroom_by_capacity_desc(self, db:Session, period:int):
        sorted_classroom = self.sort_classrom_space(self.get_by_period(period))
        classrooms = []
        for space in sorted_classroom:
            if (space.schedule_assignment == None):
                classrooms.append(space)
        return classrooms