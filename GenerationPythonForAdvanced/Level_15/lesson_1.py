# 1. Напишите функцию matrix(), которая создает, заполняет и возвращает матрицу заданного размера. При этом
# (в зависимости от переданных аргументов) она должна вести себя так:
# matrix() — возвращает матрицу 1×1, в которой единственное число равно нулю;
# matrix(n) — возвращает матрицу n×n, заполненную нулями;
# matrix(n, m) — возвращает матрицу из n строк и m столбцов, заполненную нулями;
# matrix(n, m, value) — возвращает матрицу из n строк и m столбцов, в которой каждый элемент равен числу value.
def matrix(n=None, m=None, value=0):
    if n is not None and m is None:
      mat = [[value for _ in range(n)] for _ in range(n)]
    elif n is None and m is None:
      mat = [[value for _ in range(1)] for _ in range(1)]
    else:
      mat = [[value for _ in range(m)] for _ in range(n)]
    return mat

print(matrix(2,5))