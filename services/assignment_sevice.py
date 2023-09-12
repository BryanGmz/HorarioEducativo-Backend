from sqlalchemy.orm import Session
from repositories import assignment
from objects.objects import AssignmentData

def get_assignments(db:Session):
    assignments = []
    for assigment in assignment.get_all_assignments(db):
        assignments.append(
            AssignmentData(
                assigned = assigment.assigned,
                carrer = assigment.carrer,
                course = assigment.course,
                section = "",
                year = assigment.year,
            )
        )
    return assignments