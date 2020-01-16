import random
from matrix_class import Matrix

class Vertical_vector(Matrix):
    def __init__(self, row, num, array = None):
        Matrix.__init__(self, row, 1, num)
        self.__row = row
        self.__num = num
        self.__col = 1
        if array is not None:
            self.__m = array
        else:
            self.__m = [[random.randint(0, self.__num) for n in range(self.__col)] for n in range(self.__row)]
