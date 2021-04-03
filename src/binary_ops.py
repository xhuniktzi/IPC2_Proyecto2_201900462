from models import Matriz
from Excepts import MatrixSizeException


def union_matrix(matrix_1: Matriz, matrix_2: Matriz):
    if (matrix_1.m != matrix_2.m) or (matrix_1.n != matrix_2.n):
        raise MatrixSizeException
        # return None

    name_matrix = '{}Union{}'.format(matrix_1.name, matrix_2.name)
    x_size = matrix_1.m
    y_size = matrix_2.n

    result_matrix = Matriz(name_matrix, x_size, y_size)

    count_x = 0
    while count_x < x_size:
        count_y = 0
        while count_y < y_size:
            if (matrix_1.get(count_x, count_y) == '*') or (matrix_2.get(
                    count_x, count_y) == '*'):
                result_matrix.insert(count_x, count_y, '*')
            else:
                result_matrix.insert(count_x, count_y, '-')
            count_y = count_y + 1
        count_x = count_x + 1

    return result_matrix


def intersec_matrix(matrix_1: Matriz, matrix_2: Matriz):
    if (matrix_1.m != matrix_2.m) or (matrix_1.n != matrix_2.n):
        raise MatrixSizeException
        # return None

    name_matrix = '{}Intersec{}'.format(matrix_1.name, matrix_2.name)
    x_size = matrix_1.m
    y_size = matrix_2.n

    result_matrix = Matriz(name_matrix, x_size, y_size)

    count_x = 0
    while count_x < x_size:
        count_y = 0
        while count_y < y_size:
            if (matrix_1.get(count_x, count_y) == '*') and (matrix_2.get(
                    count_x, count_y) == '*'):
                result_matrix.insert(count_x, count_y, '*')
            else:
                result_matrix.insert(count_x, count_y, '-')
            count_y = count_y + 1
        count_x = count_x + 1

    return result_matrix