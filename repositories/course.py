from sqlalchemy.orm import Session
from models.models import Course

def get_course_by_id(db:Session, id):
    return db.query(Course).filter(Course.id_course == id).first()

def get_all_course(db:Session):
    return db.query(Course).all()