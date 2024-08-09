# 1. На вход программе подаются два натуральных числа n и m. Напишите программу для создания матрицы размером n×m,
# заполнив её символами . и * в шахматном порядке. В левом верхнем углу должна стоять точка.
# Выведите полученную матрицу на экран, разделяя элементы пробелами.
n, m = map(int, input().split())
lst = [['.' for i in range(m)] for j in range(n)]
for ind, it in enumerate(lst):
    if ind % 2 == 0:
        for j in range(1, len(it), 2):
            it[j] = '*'
    if ind % 2 == 1:
        for j in range(0, len(it), 2):
            it[j] = '*'
for i in lst:
    print(*i)


# 2. На вход программе подается натуральное число n. Напишите программу, которая создает матрицу размером n×n и
# заполняет её по следующему правилу: числа на побочной диагонали равны 1; числа, стоящие выше этой диагонали, равны 0;
# числа, стоящие ниже этой диагонали, равны 2.
# Полученную матрицу выведите на экран. Числа в строке разделяйте одним пробелом.
n = int(input())
lst = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    lst[i][n-i-1] = 1
    for j in range(n):
        if ((n-j-1) < i) and ((i>=j) or (i<=j)):
            lst[i][j] = 2
for i in lst:
    print(*i)


# 3.На вход программе подаются два натуральных числа n и m. Напишите программу, которая создает матрицу размером n×m
# и заполняет её числами от 1 до n*m в соответствии с образцом.
n, m = map(int, input().split())
lst = [[0 for i in range(m)] for j in range(n)]
k = 0
for i in range(n):
    for j in range(m):
        lst[i][j] = k+1
        k += 1
for i in lst:
    for j in i:
        print(str(j).ljust(3), end='')
    print()


# 4. На вход программе подаются два натуральных числа n и m. Напишите программу,
# которая создает матрицу размером n×m, заполнив её в соответствии с образцом:
# 1  4  7  10 13 16 19
# 2  5  8  11 14 17 20
# 3  6  9  12 15 18 21
n, m = map(int, input().split())
lst = [[0 for i in range(m)] for j in range(n)]
for i in range(n):
    k = i
    for j in range(m):
        lst[i][j] = k+1
        k += n
for i in lst:
    for j in i:
        print(str(j).ljust(3), end='')
    print()


# 5. На вход программе подается натуральное число n. Напишите программу, которая создает матрицу размером n×n,
# заполнив её в соответствии с образцом:
# 1  0  0  0  1
# 0  1  0  1  0
# 0  0  1  0  0
# 0  1  0  1  0
# 1  0  0  0  1
n = int(input())
lst = [[1 if i==j or (n-i-1 == j) else 0 for i in range(n)] for j in range(n)]
for i in lst:
    for j in i:
        print(str(j).ljust(3), end='')
    print()


# 6. На вход программе подается натуральное число n. Напишите программу, которая создает матрицу размером n×n,
# заполнив её в соответствии с образцом:
# 1  1  1  1  1
# 0  1  1  1  0
# 0  0  1  0  0
# 0  1  1  1  0
# 1  1  1  1  1
n = int(input())
lst = [[1 if i==j or (n-i-1 == j) or (i>n-1-j and i<j) or (i<n-1-j and i>j) else 0 for i in range(n)] for j in range(n)]
for i in lst:
    for j in i:
        print(str(j).ljust(3), end='')
    print()


# 7.На вход программе подаются два натуральных числа n и m. Напишите программу, которая создает матрицу размером n×m,
# заполнив её в соответствии с образцом: (--)
# 1 2 3 4 5 6 7
# 2 3 4 5 6 7 1
# 3 4 5 6 7 1 2
n, m = [int(num) for num in input().split()]
matrix = [num for num in range(1, m + 1)]
for i in range(n):
    for j in range(m):
        print(matrix[j], end=' ')
    pop = matrix.pop(0)
    matrix.append(pop)
    print()


# 8. На вход программе подаются два натуральных числа n и m. Напишите программу, которая создает матрицу размером n×m,
# заполнив её "змейкой" в соответствии с образцом:
# 1  2  3  4  5
# 10 9  8  7  6
# 11 12 13 14 15
n, m = map(int, input().split())
lst = [[0 for i in range(m)] for j in range(n)]
k = 1
for i in range(n):
    for j in range(m):
        lst[i][j] = k
        k += 1
for ind, it in enumerate(lst):
    if ind % 2 != 0:
        it = it.reverse()
for i in lst:
    for j in i:
        print(str(j).ljust(3), end='')
    print()
