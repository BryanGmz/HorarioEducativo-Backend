from sqlalchemy.orm import Session
from repositories import teacher

def get_teachers(db:Session):
    return teacher.get_all_teachers(db)