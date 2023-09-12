from sqlalchemy import desc, func
from sqlalchemy.orm import Session
from models.models import Assignment

def get_assignment_by_composite_key(db:Session, course_id, carrer_id, year, semester):
    return db.query(Assignment).filter(Assignment.course_id == course_id, Assignment.carrer_id == carrer_id, Assignment.year == year, Assignment.semester == semester).first()

def get_all_assignments(db:Session):
    return db.query(Assignment).order_by(desc(Assignment.assigned)).all()

def get_assigned_by_year(year, db:Session):
    return db.query(func.sum(Assignment.assigned)).filter_by(year=year).scalar()