from pydantic import BaseModel, EmailStr, field_validator, Field
from typing import Optional, List
class User(BaseModel):
    name: str
    age: int 
    email: str
    is_active: bool = True

user_data = {
    "name": "John Doe",
    "age": 30,
    "email": "l0tZP@example.com",
}

user = User(**user_data)
print(f"Имя {user.name}, возраст {user.age}, email {user.email}, активен {user.is_active}")
print(f"Активен: {user.is_active}")

class Product(BaseModel):
    title: str = Field(... , min_length=1, max_length=100)
    price: float = Field(..., gt=0)
    quantity: int = Field(default=1, ge=0)
    tags: List[str] = []

    @field_validator("title")
    def validate_title(cls, v):
        if not v.strip():
            raise ValueError("Title is empty")
        return v.strip()

try:
    product = Product(
        title=" Телефон ",
        price = 999.99,
        quantity=5,
        tags = ['electronica, mobilki']
    )
    print(f'Продукт: {product.title}, цена: {product.price}')
except Exception as e:
    print(f'Ошибка валидации: {e}')
