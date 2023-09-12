from sqlalchemy.orm import Session
from repositories import classroom

def get_classrooms(db:Session):
    return classroom.get_all_clasroom_asc(db)