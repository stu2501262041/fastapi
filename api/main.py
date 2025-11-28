from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy.testing import db

from database import SessionLocal, Base, engine
from models import User, Movie
from schemas import MovieCreate

app = FastAPI()


Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"Hello": "World"}


##@app.post("/movie/", response_model=Movie)
##def create_movie(movie: MovieCreate, db: Session = Depends(get_db())):
    ##        db_movie = Movie(title=movie.title, genre=movie.genre, year=movie.year)
    ##   db.add(db_movie)
    ##  db.commit()
    ##  db.refresh(db_movie)
    ##  return db_movie



