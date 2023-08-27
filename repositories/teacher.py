from sqlalchemy.orm import Session
from models.models import Teacher

def get_teacher_by_dpi(db:Session, dpi):
    return db.query(Teacher).filter(Teacher.dpi_teacher == dpi).first()

def get_all_teacher(db:Session):
    return db.query(Teacher).all()