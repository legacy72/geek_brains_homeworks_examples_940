"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц)
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.
"""
import random


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        res = ''
        for row in self.matrix:
            res += f'{" ".join([str(l) for l in row])}\n'
        return res

    def __add__(self, other):
        new_matrix = [[] for _ in range(len(self.matrix))]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                new_matrix[i].append(self.matrix[i][j] + other.matrix[i][j])
        return Matrix(new_matrix)


m_1 = Matrix([[random.randint(0, 10) for _ in range(3)], [random.randint(0, 10) for _ in range(3)]])
m_2 = Matrix([[random.randint(0, 10) for _ in range(3)], [random.randint(0, 10) for _ in range(3)]])

print(f'1 matrix:\n{m_1}')
print(f'2 matrix:\n{m_2}')
m_3 = m_1 + m_2
print(f'SUM 1 and 2 matrix:\n{m_3}')
