def validate_user_data(data: dict):

    if not isinstance(data.get('first_name'), str) and len(data['first_name'].strip()) == 0:
        raise ValueError('Поле first_name должно быть непустой строкой')

    if not isinstance(data.get('last_name'), str) and len(data['last_name'].strip()) == 0:
        raise ValueError('Поле last_name должно быть непустой строкой')

    if not isinstance(data.get('age'), int) and data['age'] < 18 or data['age'] > 99:
        raise ValueError('Возраст должен быть числом от 18 до 99')

    if not isinstance(data.get('phone_number'), str):
        raise ValueError('Номер телефона должен быть строкой')

    if not isinstance(data.get('city'), str) and len(data['city'].strip()) == 0:
        raise ValueError('Город должен быть непустой строкой')

    if data.get('address') is None:
        raise ValueError('Адрес не может быть None')

    if "email" in data and ''@'' not in data['email']:
        raise ValueError('Email должен содержать @')