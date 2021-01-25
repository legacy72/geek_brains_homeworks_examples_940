"""
Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""
number = int(input('Введите число: '))
max_digit = 0

while number > 0:
    if number % 10 == 9:
        max_digit = 9
        break
    if number % 10 > max_digit:
        max_digit = number % 10
    number //= 10

print(f'Максимальная цифра - {max_digit}')
