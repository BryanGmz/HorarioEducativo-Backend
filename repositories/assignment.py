from sqlalchemy.orm import Session
from models.models import Assignment

def get_assignment_by_composite_key(db:Session, course_id, carrer_id, year, semester):
    return db.query(Assignment).filter(Assignment.course_id == course_id, Assignment.carrer_id == carrer_id, Assignment.year == year, Assignment.semester == semester).first()

def get_all_assignment(db:Session):
    return db.query(Assignment).all()