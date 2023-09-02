from sqlalchemy.orm import Session
from models.models import Teacher
from datetime import time

def get_teacher_by_dpi(db:Session, dpi):
    return db.query(Teacher).filter(
        Teacher.dpi_teacher == dpi
        ).first()

def get_all_teacher(db:Session):
    return db.query(Teacher).all()

def get_teacher_by_contracting_hour(db: Session, start_time: time, end_time: time):
    return db.query(Teacher).filter(
        (Teacher.start_contracting_hour >= start_time) |
        (Teacher.end_contracting_hour <= end_time)
    ).all()