from sqlalchemy.orm import Session
from models.models import Teacher
from datetime import time

def get_teacher_by_dpi(db:Session, dpi):
    return db.query(Teacher).filter(
        Teacher.dpi_teacher == dpi
        ).first()

def get_all_teachers(db:Session):
    return db.query(Teacher).all()

def get_teacher_by_contracting_hour(db: Session, start_time: time, end_time: time):
    return db.query(Teacher).filter(
        (start_time >= Teacher.start_conntracting_hour) &
        (end_time <= Teacher.end_conntracting_hour)
    ).all()

def create_teacher(teacher:Teacher, db:Session):
    db.add(teacher)
    db.commit()
    db.refresh(teacher)
    return teacher

def delete_teacher(dpi:int, db:Session):
    carrer = db.query(Teacher).filter(Teacher.dpi_teacher == dpi)
    if not carrer.first():
        return False
    carrer.delete(synchronize_session=False)
    db.commit()
    return True