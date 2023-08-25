from typing import Union
from config.database import Base, engine, get_db
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from models.models import Course
import uvicorn

def create_tables():
    Base.metadata.create_all(bind=engine)

create_tables()

app = FastAPI()

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)

@app.get("/")
def read_root(db:Session = Depends(get_db)):
    data = db.query(Course).all()
    print(data)
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}