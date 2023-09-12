from sqlalchemy.orm import Session
from repositories import carrer

def get_carrers(db:Session):
    return carrer.get_all_carrers(db)