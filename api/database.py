from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URL = "sqlite:///./movies.db"
##tells sqlalchemy where to find my database file


engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
##connects fastapi to the database

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
##used to interact with the database; autocommit=False - makes sure changes are not automatically made to the database


Base = declarative_base()
##foundation to all database models, helps sqlalchemy manage the models and map them to database tables


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()