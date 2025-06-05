from fastapi import FastAPI
from pydantic import BaseModel
from typing import list, Optional
app = FastAPI()

class User(BaseModel):
    name: str,
    last_name: str,
    age: int,
    phone_number: int,
    address: str,
    email: Optional[str] = None

user_data = []

@app.get('/users', response_model=list[User])
def get_users():
    return user_data

@app.post('/users')
def add_user(user: User):
    user_data.append(user.dict())
    return {'status': 'Пользователь добавлен', 'data': user}

app.get('/users/name/{name}')
def find_by_name(name: str):
    result = [i for i in user_data if i['name'].lower() == name.lower()]
    return {'status': 'Пользователь найден', 'data': result} if result else {'status': 'Нет совпадений'}

app.get('/users/last_name/{last_name}')
def find_by_last_name(last_name: str):
    result = [i for i in user_data if i['last_name'].lower() == last_name.lower()]
    return {'status': 'Пользователь найден', 'data': result} if result else {'status': 'Нет совпадений'}

app.get('/users/phone_number/{phone_number}')
def find_by_phone_number(phone_number: int):
    result = [i for i in user_data if i['phone_number'] == phone_number]
    return {'status': 'Пользователь найден', 'data': result} if result else {'status': 'Пользователь не найден'}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=80)

