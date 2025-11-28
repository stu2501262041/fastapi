from sqlalchemy.orm import Session
import models, schemas


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_users(db: Session):
    return db.query(models.User).all()


def update_user(db: Session, user_id: int, user_data: schemas.UserUpdate):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user is None:
        return None

    for key, value in user_data.dict(exclude_unset=True).items():
        setattr(user, key, value)

    db.commit()
    db.refresh(user)
    return user


def delete_user(db: Session, user_id: int):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user is None:
        return None
    db.delete(user)
    db.commit()
    return user


def create_movie(db: Session, movie: schemas.MovieCreate):
    db_movie = models.Movie(
        title=movie.title,
        genre=movie.genre,
        release_year=movie.release_year
    )
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie


def get_movies(db: Session):
    return db.query(models.Movie).all()


def update_movie(db: Session, movie_id: int, movie_data: schemas.MovieUpdate):
    movie = db.query(models.Movie).filter(models.Movie.id == movie_id).first()
    if movie is None:
        return None

    for key, value in movie_data.dict(exclude_unset=True).items():
        setattr(movie, key, value)

    db.commit()
    db.refresh(movie)
    return movie


def delete_movie(db: Session, movie_id: int):
    movie = db.query(models.Movie).filter(models.Movie.id == movie_id).first()
    if movie is None:
        return None
    db.delete(movie)
    db.commit()
    return movie


def create_actor(db: Session, actor: schemas.ActorCreate):
    db_actor = models.Actor(name=actor.name)
    db.add(db_actor)
    db.commit()
    db.refresh(db_actor)
    return db_actor


def get_actors(db: Session):
    return db.query(models.Actor).all()


def update_actor(db: Session, actor_id: int, actor_data: schemas.ActorUpdate):
    actor = db.query(models.Actor).filter(models.Actor.id == actor_id).first()
    if actor is None:
        return None

    for key, value in actor_data.dict(exclude_unset=True).items():
        setattr(actor, key, value)

    db.commit()
    db.refresh(actor)
    return actor


def delete_actor(db: Session, actor_id: int):
    actor = db.query(models.Actor).filter(models.Actor.id == actor_id).first()
    if actor is None:
        return None
    db.delete(actor)
    db.commit()
    return actor


def create_review(db: Session, review: schemas.ReviewCreate):
    db_review = models.Review(
        score=review.score,
        user_id=review.user_id,
        movie_id=review.movie_id
    )
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review


def get_reviews(db: Session):
    return db.query(models.Review).all()


def update_review(db: Session, review_id: int, review_data: schemas.ReviewUpdate):
    review = db.query(models.Review).filter(models.Review.id == review_id).first()
    if review is None:
        return None

    for key, value in review_data.dict(exclude_unset=True).items():
        setattr(review, key, value)

    db.commit()
    db.refresh(review)
    return review


def delete_review(db: Session, review_id: int):
    review = db.query(models.Review).filter(models.Review.id == review_id).first()
    if review is None:
        return None
    db.delete(review)
    db.commit()
    return review
