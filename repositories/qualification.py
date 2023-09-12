from sqlalchemy import desc
from sqlalchemy.orm import Session
from models.models import Qualification

def get_qualification_by_teacher_and_is_owner(db:Session, dpi):
      return db.query(Qualification).filter(Qualification.teacher_dpi == dpi).order_by(desc(Qualification.is_owner)).all()

def get_qualification_by_course(db:Session, id):
       return db.query(Qualification).filter(Qualification.course_id == id).all()

def get_qualification_by_composite_key(db:Session, course_id, dpi):
    return db.query(Qualification).filter(Qualification.course_id == course_id, Qualification.teacher_dpi == dpi).order_by(desc(Qualification.is_owner)).first()