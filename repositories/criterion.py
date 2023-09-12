from sqlalchemy.orm import Session
from models.models import Criterion

def get_criterion_by_id(db:Session, id):
    return db.query(Criterion).filter(Criterion.id_criterion == id).first()

def get_all_criterion(db:Session):
    return db.query(Criterion).all()