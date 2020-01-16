import random
from matrix_class import Matrix

class Horizontal_vector(Matrix):
    def __init__(self, col, num, array = None):
        Matrix.__init__(self, 1, col, num)
        self.__row = 1
        self.__num = num
        self.__col = col
        if array is not None:
            self.__m = array
        else:
            self.__m = [random.randint(0, self.__num) for n in range(self.__col)]
