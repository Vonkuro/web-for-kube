from typing import Union
from pydantic import BaseModel

class UserBase(BaseModel):
    """
        Classe interface base User
    """
    name: str
    fullname: str

class User(UserBase):
    """
        Classe interface User
    """
    id: int

class UserCreate(UserBase):
    """
        Classe interface User Create
    """
