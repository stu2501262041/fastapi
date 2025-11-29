from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from database import Base

movie_actor = Table(
    "movie_actor",
    Base.metadata,
    Column("movie_id", ForeignKey("movies.id"), primary_key=True),
    Column("actor_id", ForeignKey("actors.id"), primary_key=True),
)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    reviews = relationship("Review", back_populates="user")


class Movie(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True)
    genre = Column(String)
    release_year = Column(Integer)
    reviews = relationship("Review", back_populates="movie")
    actors = relationship("Actor", secondary=movie_actor, back_populates="movies")


class Actor(Base):
    __tablename__ = "actors"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    movies = relationship("Movie", secondary=movie_actor, back_populates="actors")


class Review(Base):
    __tablename__ = "reviews"
    id = Column(Integer, primary_key=True)
    score = Column(Integer)
    user_id = Column(Integer, ForeignKey("users.id"))
    movie_id = Column(Integer, ForeignKey("movies.id"))
    user = relationship("User", back_populates="reviews")
    movie = relationship("Movie", back_populates="reviews")



