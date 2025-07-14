from datetime import date
from pkgutil import get_data
from fastapi import FastAPI, HTTPException, status
from uuid import UUID, uuid4
from models import User, UserCreate, UserUpdate
from utils import generate_fake_user
from typing import Dict, List


app = FastAPI(title="User Managment API")

fake_db: Dict[UUID, User] = {}

@app.get("/users", response_model=List[User])

def get_users():
    return list(fake_db.values())

@app.get("/")
def root():
    return {"message": "Добро пожаловать в User Management API!"}

@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: UUID):
    user = fake_db.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return user

@app.post("/users", response_model=User, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate):
    user = User(
    id=uuid4(),
    first_name=get_data.first_name,
    last_name=get_data.last_name,
    email=get_data.email,
    registration_date=date.today(),
    is_active=get_data.is_active,
    address=get_data.address,
    phone_number=get_data.phone_number
)
    fake_db[user.id] = user
    return user

@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: UUID, user_data: UserUpdate):
    if user_id not in fake_db:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    update_user = User(id=user_id, registered_date=fake_db[user_id].registered_date, **user_data.dict())
    fake_db[user_id] = update_user
    return update_user

@app.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: UUID):
    if user_id not in fake_db:
         raise HTTPException(status_code=404, detail="Пользователь не найден")
    del fake_db[user_id]