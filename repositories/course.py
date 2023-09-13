from sqlalchemy.orm import Session
from models.models import Course

def get_course_by_id(db:Session, id):
    return db.query(Course).filter(Course.id_course == id).first()

def get_all_courses(db:Session):
    return db.query(Course).all()

def create_course(course:Course, db:Session):
    db.add(course)
    db.commit()
    db.refresh(course)
    return course

def delete_course(id:int, db:Session):
    carrer = db.query(Course).filter(Course.id_course == id)
    if not carrer.first():
        return False
    carrer.delete(synchronize_session=False)
    db.commit()
    return True