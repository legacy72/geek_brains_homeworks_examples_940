"""
Создать вручную и заполнить несколькими строками текстовый файл,
в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""
import json

READ_FILE_NAME = 'files/task_7.txt'
WRITE_FILE_NAME = 'files/task_7.json'
COUNT_POSITIVE_INCOME = 0


with open(READ_FILE_NAME, 'r', encoding='UTF-8') as f:
    sum_profit = 0
    res = {}
    lines = f.readlines()
    for line in lines:
        name, form, income, outcome = line.split()
        profit = float(income) - float(outcome)
        res[name] = profit
        if profit > 0:
            sum_profit += profit
            COUNT_POSITIVE_INCOME += 1

res['average_profit'] = round(sum_profit / COUNT_POSITIVE_INCOME, 2)

with open(WRITE_FILE_NAME, 'w', encoding='UTF-8') as f:
    json.dump(res, f)
