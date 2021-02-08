"""
Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
"""
FILE_NAME = 'files/task_2.txt'

with open(FILE_NAME, 'r', encoding='UTF-8') as f:
    lines = f.readlines()
print(f'Кол-во строк в файле: {len(lines)}')
for i, line in enumerate(lines, 1):
    print(f'Кол-во слов в {i} строке: {len(line.split())}')
