import os
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from src.models import Base as BaseModel
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

database_path = os.getenv('DATABASE_PATH')

def engine():
    """
        Connexion à la base de donnée dev
    """
    return create_engine("sqlite:///" +  database_path + "user.db", echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine())

Base = declarative_base()

def get_db():
    """
        Créer et retourne une instance la connexion à la base de donnée
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_tables():
    """
        Test la connexion.
        Provoque une exception si l'api n'arrive pas à se connecter à la base de données
    """
    BaseModel.metadata.create_all(engine())
