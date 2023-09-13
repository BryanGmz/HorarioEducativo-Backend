from sqlalchemy.orm import Session
from models.models import Carrer

def get_carrer_by_id(db:Session, id):
    return db.query(Carrer).filter(Carrer.id_carrer == id).first()

def get_all_carrers(db:Session):
    return db.query(Carrer).all()

def create_carrer(carrer:Carrer, db:Session):
    db.add(carrer)
    db.commit()
    db.refresh(carrer)
    return carrer

def delete_carrer(id:int, db:Session):
    carrer = db.query(Carrer).filter(Carrer.id_carrer == id)
    if not carrer.first():
        return False
    carrer.delete(synchronize_session=False)
    db.commit()
    return True