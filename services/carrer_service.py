from sqlalchemy.orm import Session
from repositories import carrer
from schemas.schemas import CreateCarrer
from models.models import Carrer
from fastapi import HTTPException, status 

def get_carrers(db:Session):
    return carrer.get_all_carrers(db)

def create_carrer(carrer_data:CreateCarrer, db:Session):
    try:
        carrer_db = Carrer(
            name = carrer_data.name
        )
        carrer.create_carrer(carrer_db, db)
    except Exception as e :
        raise HTTPException(
            status_code = status.HTTP_409_CONFLICT,
            detail = f"Error creando la carera {e}"
        )
    
def delete_carrer(id:int, db:Session):
    if (carrer.delete_carrer(id, db)):
        return {
            "response": "Carrera eliminada satisfactoriamente."
        }
    raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail=f"No existe la carrera con el id {id} por lo tanto no se elimina."
        )
