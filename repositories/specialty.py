from sqlalchemy.orm import Session
from models.models import Specialty

def get_area_by_composite_key(db:Session, area_id, teacher_dpi):
    return db.query(Specialty).filter(Specialty.area_id == area_id, Specialty.teacher_dpi == teacher_dpi).first()

def get_all_specialty(db:Session):
    return db.query(Specialty).all()