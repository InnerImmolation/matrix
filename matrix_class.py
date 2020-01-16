import random


def list_sum(list1, list2):
    min_len = min(len(list1), len(list2))
    return [list1[i] + list2[i] for i in range(min_len)]


def list_diff(list1, list2):
    min_len = min(len(list1), len(list2))
    return [list1[i] - list2[i] for i in range(min_len)]


def row_check(row, diag_element):
    for i in range(len(row)):
        if i == diag_element:
            continue
        if row[i] != 0:
            return False
    return True


class Matrix:
    def __init__(self, row, col, num, array=None):
        self.__row = row
        self.__col = col
        self.__num = num
        if array is not None and self.__row == len(array) and self.__col == len(array[0]):
            self.__m = array
        elif array is not None and self.__row != len(array) and self.__col != len(array[0]):
            raise ValueError("Размер матрицы не соответствует указанным значениям")
        else:
            self.__m = [[random.randint(0, self.__num) for n in range(self.__col)] for n in range(self.__row)]

    def __add__(self, other):
        min_len = min(len(self.__m), len(other.__m))
        return Matrix(len(self.__m[0]), min_len, 1, [list_sum(self.__m[i], other.__m[i]) for i in range(min_len)]).matrix_print

    def __sub__(self, other):
        min_len = min(len(self.__m), len(other.__m))
        return Matrix(len(self.__m[0]), min_len, 1, [list_diff(self.__m[i], other.__m[i]) for i in range(min_len)]).matrix_print

    def __mul__(self, other):
        s = 0
        t = []
        m3 = []
        if len(other.__m) != len(self.__m[0]):
            raise ValueError("Матрицы не могут быть перемножены")
        else:
            r1 = len(self.__m)
            c1 = len(self.__m[0])
            c2 = len(other.__m[0])
            for z in range(0, r1):
                for j in range(0, c2):
                    for i in range(0, c1):
                        s = s + self.__m[z][i] * other.__m[i][j]
                    t.append(s)
                    s = 0
                m3.append(t)
                t = []
        return Matrix(len(self.__m[0]), len(self.__m), 1, m3).matrix_print

    @property
    def matrix_print(self):
        return '\n'.join(' '.join(str(x) for x in line) for line in self.__m)

    @property
    def matrix_transpose(self):
        rows = len(self.__m)
        column = len(self.__m[0])
        return Matrix(rows, column, 1, [sum([[self.__m[j][i]] for j in range(column)], []) for i in range(rows)]).matrix_print

    @property
    def is_diagonal(self):
        rows = len(self.__m)
        for i in range(rows):
            if not row_check(self.__m[i], i):
                return False
        return True

    @property
    def is_zero(self):
        for line in self.__m:
            for x in line:
                if x != 0:
                    return False
        return True

    @property
    def is_identity(self):
        return True if (len(self.__m) == 1 and len(self.__m[0]) == 1) else False
    @property
    def is_square(self):
        return True if (len(self.__m) == len(self.__m[0]) ) else False
