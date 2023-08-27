from sqlalchemy.orm import Session
from models.models import ScheduleAssignment

def create_schedule_assignament(db:Session, user):
    db.add(user)
    db.commit()
    db.flush(user)
    return user

def get_all_schedule_assignment(db:Session):
    return db.query(ScheduleAssignment).all()