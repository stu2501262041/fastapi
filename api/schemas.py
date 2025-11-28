from typing import Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class MovieBase(BaseModel):
    title: str
    genre: str
    release_year: int


class MovieCreate(BaseModel):
    title: str
    genre: str
    year: int


class Movie(BaseModel):
    id: int

    class Config:
        orm_mode = True


class ActorBase(BaseModel):
    name: str


class ActorCreate(ActorBase):
    pass


class Actor(ActorBase):
    id: int

    class Config:
        orm_mode = True


class ReviewBase(BaseModel):
    text: str
    rating: int


class ReviewCreate(ReviewBase):
    user_id: int


class Review(ReviewBase):
    id: int
    movie_id: int
    user_id: int

    class Config:
        orm_mode = True


class MovieUpdate(BaseModel):
    title: Optional[str] = None
    genre: Optional[str] = None
    release_year: Optional[int] = None


class ReviewUpdate(BaseModel):
    text: Optional[str] = None
    rating: Optional[int] = None


class UserUpdate(BaseModel):
    name: Optional[str] = None


class ActorUpdate(BaseModel):
    name: Optional[str] = None
