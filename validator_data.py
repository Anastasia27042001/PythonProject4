def validate_user_data(data: dict):
    print("Данные на входе:", data)
    first_name = data.get('first_name')
    if not isinstance(first_name, str) or not first_name.strip():
        raise ValueError('Поле first_name должно быть непустой строкой')

    last_name = data.get('last_name')
    if not isinstance(last_name, str) or not last_name.strip():
        raise ValueError('Поле last_name должно быть непустой строкой')

    age = data.get('age')
    if not isinstance(age, int) or age < 18 or age > 99:
        raise ValueError('Возраст должен быть числом от 18 до 99')

    phone_number = data.get('phone_number')
    if not isinstance(phone_number, str) or (9 <= len(phone_number) <= 18) == False :
        raise ValueError('Номер телефона должен быть строкой')

    address = data.get('address')
    if not isinstance(address, str):
        raise ValueError('Адрес должен быть строкой')
    if not address.strip():
        raise ValueError('Адрес не может быть пустым')

    email = data.get('email')
    if email and '@' not in email:
        raise ValueError('Email должен содержать @')