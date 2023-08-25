from sqlmodel import Session, create_engine, SQLModel
from utils import get_database

engine = create_engine(get_database())
session = Session(engine)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def main():
    create_db_and_tables()


def get_session():
    db=session
    try:
        yield db
    finally:
        db.close()
