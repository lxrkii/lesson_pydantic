from faker import Faker
from uuid import uuid4
from datetime import date
from models import User

faker = Faker('ru_RU')

def generate_fake_user():
    return User(
        id = uuid4(),
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        email=faker.email(),
        registered_date=faker.date_between(start_date='-10y', end_date='today'),
        is_active=faker.boolean(),
        address=faker.address().replace('\n', ',  '),
        phone_number=faker.phone_number()
    )