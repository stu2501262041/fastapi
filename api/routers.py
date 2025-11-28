from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import crud, schemas

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/users", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)


@router.get("/users", response_model=list[schemas.User])
def read_users(db: Session = Depends(get_db)):
    return crud.get_users(db)


@router.post("/movies", response_model=schemas.Movie)
def create_movie(movie: schemas.MovieCreate, db: Session = Depends(get_db)):
    return crud.create_movie(db, movie)


@router.get("/movies", response_model=list[schemas.Movie])
def read_movies(db: Session = Depends(get_db)):
    return crud.get_movies(db)


@router.post("/actors", response_model=schemas.Actor)
def create_actor(actor: schemas.ActorCreate, db: Session = Depends(get_db)):
    return crud.create_actor(db, actor)


@router.get("/actors", response_model=list[schemas.Actor])
def read_actors(db: Session = Depends(get_db)):
    return crud.get_actors(db)


@router.post("/reviews", response_model=schemas.Review)
def create_review(review: schemas.ReviewCreate, db: Session = Depends(get_db)):
    return crud.create_review(db, review)


@router.get("/review", response_model=list[schemas.Review])
def read_reviews(db: Session = Depends(get_db)):
    return crud.get_reviews(db)