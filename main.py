from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
from validator_data import validate_user_data
app = FastAPI()

class User(BaseModel):
    first_name: str
    last_name: str
    age: int
    phone_number: str
    city: str
    address: str
    email: str

user_data = []

@app.get('/users', response_model=List[User])
def get_users():
    return user_data

@app.post('/users')
def add_user(user: User):
    user_data.append(user.dict())
    return {'status': 'Пользователь добавлен', 'data': user}

app.get('/users/name/{name}')
def find_by_name(first_name: str):
    result = [i for i in user_data if i['first_name'].lower() == first_name.lower()]
    return {'status': 'Пользователь найден', 'data': result} if result else {'status': 'Нет совпадений'}

app.get('/users/last_name/{last_name}')
def find_by_last_name(last_name: str):
    result = [i for i in user_data if i['last_name'].lower() == last_name.lower()]
    return {'status': 'Пользователь найден', 'data': result} if result else {'status': 'Нет совпадений'}

app.get('/users/phone_number/{phone_number}')
def find_by_phone_number(phone_number: int):
    result = [i for i in user_data if i['phone_number'] == phone_number]
    return {'status': 'Пользователь найден', 'data': result} if result else {'status': 'Пользователь не найден'}

app.get('/users/city/{city}')
def find_by_city(city: str):
    result = [i for i in user_data if i['city'].lower() == city.lower()]
    return {'status': 'Пользователи найдены', 'data': result} if result else {'status': 'Пользователи не найден'}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

