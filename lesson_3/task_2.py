"""
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def person_info(first_name, second_name, date_of_birth, city, email, phone):
    return f'{second_name} {first_name}\n' \
           f'Дата рождения: {date_of_birth}\n' \
           f'Город: {city}\n' \
           f'Почта: {email}\n' \
           f'Телефон: {phone}'


print(person_info(
    first_name=input('Введите имя: '),
    second_name=input('Введите фамилию: '),
    date_of_birth=input('Введите дату рождения: '),
    city=input('Введите город: '),
    email=input('Введите почту: '),
    phone=input('Введите телефон: '),
))
