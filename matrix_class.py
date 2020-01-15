import random


class Matrix:
    def __init__(self, row, col, num):
        self.__row = row
        self.__col = col
        self.__num = num
        self.__m = [[random.randint(0, self.__num) for n in range(self.__col)] for n in range(self.__row)]

    def __add__(self, other):
        min_len = min(len(self.__m), len(other.__m))
        return [list_sum(self.__m[i], other.__m[i]) for i in range(min_len)]

    @property
    def matrix_print(self):
        return '\n'.join(' '.join(str(x) for x in line) for line in self.__m)


def list_sum(list1, list2):
    min_len = min(len(list1), len(list2))
    return [list1[i] + list2[i] for i in range(min_len)]


def list_diff(list1, list2):
    min_len = min(len(list1), len(list2))
    return [list1[i] - list2[i] for i in range(min_len)]


def matrix_sum(matrix1, matrix2):
    min_len = min(len(matrix1), len(matrix2))
    return [list_sum(matrix1[i], matrix2[i]) for i in range(min_len)]


def matrix_dif(matrix1, matrix2):
    min_len = min(len(matrix1), len(matrix2))
    return [list_diff(matrix1[i], matrix2[i]) for i in range(min_len)]


def matrix_multy(m1, m2):
    s = 0
    t = []
    m3 = []
    if len(m2) != len(m1[0]):
        raise ValueError("Матрицы не могут быть перемножены")
    else:
        r1 = len(m1)
        c1 = len(m1[0])
        c2 = len(m2[0])
        for z in range(0, r1):
            for j in range(0, c2):
                for i in range(0, c1):
                    s = s + m1[z][i] * m2[i][j]
                t.append(s)
                s = 0
            m3.append(t)
            t = []
    return m3


def matrix_transpose(matrix):
    rows = len(matrix)
    column = len(matrix[0])
    return [sum([[matrix[j][i]] for j in range(column)], []) for i in range(rows)]


def row_check(row, diag_element):
    for i in range(len(row)):
        if i == diag_element:
            continue
        if row[i] != 0:
            return False
    return True


def is_diagonal(matrix):
    rows = len(matrix)
    for i in range(rows):
        if not row_check(matrix[i], i):
            return False
    return True


m1 = Matrix(2, 2, 10)
m2 = Matrix(2, 2, 10)
print(m1 + m2)
