from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from config.database import get_db
from services import assignment_sevice
from schemas.schemas import CreateAssignment

router = APIRouter (
    prefix = "/assignment",
    tags = ["Assigment"]
)

@router.get('/all/',status_code=status.HTTP_200_OK)
def get_assignments(db:Session = Depends(get_db)):
    return {"assigments": assignment_sevice.get_assignments(db)}


@router.post('/', status_code = status.HTTP_201_CREATED)
def create_assignment(assignment_data:CreateAssignment, db:Session = Depends(get_db)):
    assignment_sevice.create_assignment(assignment_data, db)
    return {
        "response": "Asignación creada satisfactoriamente."
    }

@router.delete('/{id}', status_code = status.HTTP_200_OK)
def delete_assignment(id:int, db:Session = Depends(get_db)):
    return assignment_sevice.delete_assignment(id, db)
