from sqlalchemy import desc
from sqlalchemy.orm import Session
from models.models import Classroom

def get_classroom_by_id(db:Session, id):
    return db.query(Classroom).filter(Classroom.id_classroom == id).first()

def get_all_clasroom(db:Session):
    return db.query(Classroom).order_by(desc(Classroom.capacity)).all()

def get_all_clasroom_asc(db:Session):
    return db.query(Classroom).order_by(Classroom.id_classroom).all()

def get_first_classroom_by_capacity_desc(db:Session):
    return db.query(Classroom).order_by(desc(Classroom.capacity)).first()

def create_clasroom(classroom:Classroom, db:Session):
    db.add(classroom)
    db.commit()
    db.refresh(classroom)
    return classroom

def delete_classroom(id:int, db:Session):
    carrer = db.query(Classroom).filter(Classroom.id_classroom == id)
    if not carrer.first():
        return False
    carrer.delete(synchronize_session=False)
    db.commit()
    return True