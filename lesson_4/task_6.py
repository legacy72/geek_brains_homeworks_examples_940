"""
Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
"""
from itertools import count, cycle


print('========== Итератор, генерирующий целые числа, начиная с указанного ==========')
start = int(input('Введите число, с которого нужно начать генерацию: '))
end = int(input('Введите число, на котором следует остановиться: '))

counter = count(start)

for i in range(start, end + 1):
    print(next(counter))


cycler = cycle([1, 2, 3])
action = None
print('========== Итератор, повторяющий элементы некоторого списка, определенного заранее ==========')
print('Нажмите q, чтобы остановиться или любую другую кнопку, чтобы продолжить')
while action != 'q':
    print(next(cycler), end='')
    action = input()