from sqlalchemy.orm import Session
from models.models import Area

def get_area_by_id(db:Session, id):
    return db.query(Area).filter(Area.id_area == id).first()

def get_all_area(db:Session):
    return db.query(Area).all()