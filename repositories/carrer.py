from sqlalchemy.orm import Session
from models.models import Carrer

def get_carrer_by_id(db:Session, id):
    return db.query(Carrer).filter(Carrer.id_carrer == id).first()

def get_all_clasroom(db:Session):
    return db.query(Carrer).all()