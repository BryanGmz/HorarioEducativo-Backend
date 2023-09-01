from sqlalchemy import desc
from sqlalchemy.orm import Session
from models.models import Classroom

def get_classroom_by_id(db:Session, id):
    return db.query(Classroom).filter(Classroom.id_classroom == id).first()

def get_all_clasroom(db:Session):
    return db.query(Classroom).order_by(desc(Classroom.capacity)).all()

def get_first_classroom_by_capacity_desc(db:Session):
    return db.query(Classroom).order_by(desc(Classroom.capacity)).first()