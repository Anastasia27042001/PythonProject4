from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from validator_data import validate_user_data
from fastapi import HTTPException
app = FastAPI()

user_data = []

class User(BaseModel):
    first_name: str
    last_name: str
    age: int
    phone_number: str
    address: str
    email: str

@app.get('/users', response_model=List[User])
def get_users():
    return user_data

@app.post('/users')
def add_user(user: User):
    try:
        user_dict = user.dict()
        validate_user_data(user_dict)
        user_data.append(user_dict)
        return {'status': 'Пользователь добавлен', 'data': user}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Внутренняя ошибка сервера")

@app.get('/users/first_name/{first_name}')
def find_by_name(first_name: str):
    result = [i for i in user_data if i['first_name'].lower() == first_name.lower()]
    return {'status': 'Пользователь найден', 'data': result} if result else {'status': 'Нет совпадений'}

@app.get('/users/last_name/{last_name}')
def find_by_last_name(last_name: str):
    result = [i for i in user_data if i['last_name'].lower() == last_name.lower()]
    return {'status': 'Пользователь найден', 'data': result} if result else {'status': 'Нет совпадений'}

@app.get('/users/phone_number/{phone_number}')
def find_by_phone_number(phone_number: int):
    result = [i for i in user_data if i['phone_number'] == phone_number]
    return {'status': 'Пользователь найден', 'data': result} if result else {'status': 'Пользователь не найден'}

@app.get('/users/address/{address}')
def find_by_address(address: str):
    result = [i for i in user_data if i['address'].lower() == address.lower()]
    return {'status': 'Пользователи найдены', 'data': result} if result else {'status': 'Пользователи не найден'}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)



