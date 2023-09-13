from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from config.database import get_db
from services import carrer_service
from schemas.schemas import CreateCarrer

router = APIRouter (
    prefix = "/carrer",
    tags = ["Carrer"]
)

@router.get('/all/', status_code = status.HTTP_200_OK)
def carrers(db:Session = Depends(get_db)):
    return {
        "carrers": carrer_service.get_carrers(db)
    }

@router.post('/', status_code = status.HTTP_201_CREATED)
def create_carrer(carrer_data:CreateCarrer, db:Session = Depends(get_db)):
    carrer_service.create_carrer(carrer_data, db)
    return {
        "response": "Carrera creada satisfactoriamente."
    }

@router.delete('/{id}', status_code = status.HTTP_200_OK)
def delete_carrer(id:int, db:Session = Depends(get_db)):
    return carrer_service.delete_carrer(id, db)