from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from config.database import get_db
from services import qualification_service
from schemas.schemas import CreateQualification

router = APIRouter (
    prefix = "/qualification",
    tags = ["Qualification"]
)

@router.get('/{dpi}/', status_code = status.HTTP_200_OK)
def get_qualification_by_dpi(dpi:int, db:Session = Depends(get_db)):
    return  {"qualifications": qualification_service.get_qualification_by_dpi(dpi, db)}

@router.post('/', status_code = status.HTTP_201_CREATED)
def create_qualification(qualification_data:CreateQualification, db:Session = Depends(get_db)):
    qualification_service.create_qualification(qualification_data, db)
    return {
        "response": "Cualificación creada satisfactoriamente."
    }

@router.delete('/{id}/', status_code = status.HTTP_200_OK)
def delete_qualification(id:int, db:Session = Depends(get_db)):
    return qualification_service.delete_qualification(id, db)