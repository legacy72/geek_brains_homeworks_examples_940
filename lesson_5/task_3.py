"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк)
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
"""
FILE_NAME = 'files/task_3.txt'

# NOTE: не учитываются пустые строки в файле с сотрудниками и их авансами
with open(FILE_NAME, 'r', encoding='UTF-8') as f:
    lines = f.readlines()

second_names_with_low_salary = []
average_salary = 0
for line in lines:
    second_name, salary = line.split()
    salary = float(salary)
    average_salary += salary
    if salary < 20000:
        second_names_with_low_salary.append(second_name)

print(f'Сотрудники с окладом меньше 20000: {second_names_with_low_salary}')
print(f'Средний оклад: {round(average_salary / len(lines), 2)}')
