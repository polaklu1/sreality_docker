import uvicorn
import os
from fastapi import FastAPI, Depends, Request
from fastapi.templating import Jinja2Templates
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel

## RUN uvicorn main:app --host 127.0.0.1 --port 8080 --reload

# SQLAlchemy setup

# DATABASE_URL = "postgresql://postgres:87654312@db:5432/postgres"
DATABASE_URL = os.getenv('DATABASE_URL')

engine = create_engine(DATABASE_URL)

Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class ItemDB(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    locality = Column(String)
    image_url = Column(String)


Base.metadata.create_all(bind=engine)

# FastAPI setup
app = FastAPI()

templates = Jinja2Templates(directory="templates")


# Pydantic model for the data
class Item(BaseModel):
    title: str
    locality: str
    image_url: str


# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        print('Connection successful')
        yield db
    finally:
        print('Connection closed')
        db.close()


@app.get("/")
async def read_items(request: Request, db: Session = Depends(get_db)):
    items = db.query(ItemDB).all()
    item_list = [Item(title=item.title, locality=item.locality, image_url=item.image_url) for item in items]

    return templates.TemplateResponse("homepage.html", {"request": request, "items": item_list})


if __name__ == '__main__':
    # uvicorn.run(app, port=8080, host="127.0.0.1")
    uvicorn.run(app, port=8080, host="0.0.0.0")
