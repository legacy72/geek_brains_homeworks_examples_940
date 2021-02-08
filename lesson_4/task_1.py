"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""
from sys import argv


def salary(hours, rate, premium):
    return f'ЗП составляет: {hours} * {rate} + {premium} = {float(hours) * float(rate) + float(premium)}'


_, hours, rate, premium = argv
print(salary(hours, rate, premium))
