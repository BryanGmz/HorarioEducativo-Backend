from sqlalchemy.orm import Session
from models.models import Classroom

def get_classroom_by_id(db:Session, id):
    return db.query(Classroom).filter(Classroom.id_classroom == id).first()

def get_all_clasroom(db:Session):
    return db.query(Classroom).all()