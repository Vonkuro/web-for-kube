from fastapi import FastAPI
from sqlalchemy.orm import Session
from src import actions, schemas, models
from fastapi import Depends
from src.database import create_tables
import src.actions as actions
from src.database import get_db

app = FastAPI()


@app.post("/create-database")
async def create_database():
    create_tables()
    return {"message": "Database created"}

@app.post("/user", response_model=schemas.User, status_code=201)
async def create_user(user: schemas.UserCreate, database: Session = Depends(get_db)):
    new_user= models.User(
            name=user.name,
            fullname=user.fullname,
        )
    
    user = actions.create_user(new_user, database)
    return user
