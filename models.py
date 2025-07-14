from pydantic import BaseModel, EmailStr, Field, validate_email
from typing import Optional
from uuid import UUID
from datetime import date

class User(BaseModel):
    id: UUID
    first_name: str
    last_name: str 
    email: EmailStr
    registered_date: date
    address: str
    phone_number: str
    is_active: bool

class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    address: str
    phone_number: str
    is_active: bool

class UserUpdate(UserCreate):
    pass
