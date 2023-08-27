from sqlalchemy.orm import Session
from models.models import Requirement

def get_requeriment_by_composite_key(db:Session, area_id, course_id):
    return db.query(Requirement).filter(Requirement.area_id == area_id, Requirement.course_id == course_id).first()

def get_all_requeriment(db:Session):
    return db.query(Requirement).all()