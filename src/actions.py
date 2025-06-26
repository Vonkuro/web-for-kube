from sqlalchemy.orm import Session
from src import models

def create_user(user: models.User, database: Session):
    """
        Créer et retourne le user
    """
    database.add(user)
    database.commit()
    database.refresh(user)
    return user

def get_users(database: Session):
    """
        Retourne la liste des users
    """
    all_users = database.query(models.User)
    return all_users