# 1. На вход программе подаются два натуральных числа n и m — количество строк и столбцов в матрице.
# Создайте матрицу mult размером n×m и заполните её таблицей умножения по формуле mult[i][j] = i * j.
# Программа должна вывести таблицу умножения отводя на вывод каждого числа ровно 3 символа
# (для этого используйте строковый метод ljust())
n = int(input())
m = int(input())
mult = [[0 for j in range(m)] for i in range(n)]
for i in range(n):
    for j in range(m):
        mult[i][j] = i*j
for i in range(n):
    for j in range(m):
        print(str(mult[i][j]).ljust(3), end=' ')
    print()


# 2. На вход программе подаются два натуральных числа n и m — количество строк и столбцов в матрице, затем n строк по
# m целых чисел в каждой, отделенных символом пробела. Напишите программу, которая находит индексы (строку и столбец)
# первого вхождения максимального элемента. Примечание: Считайте, что нумерация строк и столбцов начинается с нуля.
n = int(input())
m = int(input())
mult = [list(map(int, input().split())) for j in range(n)]
s = f'0 0'
max = mult[0][0]
for i in range(n):
    for j in range(m):
        if mult[i][j] > max:
            max = mult[i][j]
            s = f'{i} {j}'
print(s)


# 3. Напишите программу, которая меняет местами столбцы в матрице. На вход программе на разных строках подаются два
# натуральных числа n и m — количество строк и столбцов в матрице, затем элементы матрицы построчно через пробел,
# затем числа i и j — номера столбцов, подлежащих обмену.
n = int(input())
m = int(input())
mult = [list(map(int, input().split())) for j in range(n)]
s1, s2 = map(int, input().split())
for i in mult:
    k = i[s1]
    i[s1] = i[s2]
    i[s2] = k
for i in mult:
    print(*i)


# 4. Напишите программу, которая проверяет симметричность квадратной матрицы относительно главной диагонали.
# На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы матрицы
# построчно через пробел. Программа должна вывести YES, если матрица симметрична относительно главной диагонали,
# или NO в противном случае.
n = int(input())
mat = [list(map(int, input().split())) for j in range(n)]
flag = True
for i in range(n):
    for j in range(n):
        if mat[i][j] != mat[j][i]:
            flag = False
            break
if flag: print('YES')
else: print('NO')


# 5. Дана квадратная матрица чисел. Напишите программу, которая меняет местами элементы, стоящие на главной и побочной
# диагонали, при этом каждый элемент должен остаться в том же столбце (то есть в каждом столбце нужно поменять местами
# элемент на главной диагонали и на побочной диагонали). На вход программе подаётся натуральное число n — количество
# строк и столбцов в матрице, затем элементы матрицы построчно через пробел.
n = int(input())
mat = [list(map(int, input().split())) for j in range(n)]
for i in range(n):
    for j in range(n):
        if (i == j) or ((i + j + 1) == n):
            k = mat[i][i]
            mat[i][i] = mat[n-1-i][j]
            mat[n-1-i][j] = k
for i in mat:
    print(*i)


# 6. Дана квадратная матрица чисел. Напишите программу, которая зеркально отображает её элементы относительно
# горизонтальной оси симметрии.На вход программе подаётся натуральное число n — количество строк и столбцов в матрице,
# затем элементы матрицы построчно через пробел.
n = int(input())
mat = [list(map(int, input().split())) for j in range(n)]
mat = mat[::-1]
for i in mat:
    print(*i)


# 7. Напишите программу, которая поворачивает квадратную матрицу чисел на 90 градусов по часовой стрелке.
# На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы
# матрицы построчно через пробел.
n = int(input())
mat = [list(map(int, input().split())) for j in range(n)]
for i in range(n):
    for j in range(n):
        print(mat[n-1-j][i], end=' ')
    print()


# 8. На шахматной доске 8×8 стоит конь. Напишите программу, которая отмечает положение коня на доске и все клетки,
# которые бьёт конь. Клетку, где стоит конь, отметьте английской буквой N, а клетки, которые бьёт конь,
# отметьте символами *, остальные клетки заполните точками. На вход программе подаются координаты коня на шахматной
# доске в шахматной нотации (то есть в виде e4, где сначала записывается номер столбца (буква от a до h, слева направо),
# затем номеру строки (цифра от 1 до 8, снизу вверх)).
n = input()
s = 8

def str_in_digit(n):
    dd = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
    da = {'8': 0, '7': 1, '6': 2, '5': 3, '4': 4, '3': 5, '2': 6, '1': 7}
    a = dd.get(n[0])
    b = da.get(n[1])
    return a, b

def create_matrix(len, a, b):
    matrix = [['.' for i in range(len)] for j in range(len)]
    for i in range(s):
        for j in range(s):
            if i == b and j == a:
                matrix[i][j] = 'N'
    return matrix

def go_horse(matrix, a, b):
    for i in range(s):
        for j in range(s):
            if ((i == b-2) or (i == b+2)) and ((j == a-1) or (j == a+1)):
                matrix[i][j] = '*'
            if ((i == b+1) or (i == b-1)) and ((j == a+2) or (j == a-2)):
                matrix[i][j] = '*'
    return matrix

def print_mtrix_with_step(matrix):
    for i in matrix:
        print(*i)

a, b = str_in_digit(n)
matrix = create_matrix(s, a, b)
step = go_horse(matrix, a, b)
print_mtrix_with_step(step)


# 9. Магическим квадратом порядка n называется квадратная таблица размера n×n, составленная из всех чисел 1,2,3,…,n**2
# так, что суммы по каждому столбцу, каждой строке и каждой из двух диагоналей равны между собой. Напишите программу,
# которая проверяет, является ли заданная квадратная матрица магическим квадратом.
# незаконченное решение
n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
sum_all = sum(lst[1])
flag = True

lst2 = [j for i in lst for j in i]
lst2.sort()
lst3 = [i for i in range(1, (n**2)+1)]

if lst2 != lst3:
    flag = False
else:
    for i in range(n):
        sum_colum, sum_dp = 0, 0
        sum_raw = sum(lst[i])
        for j in range(n):
            sum_colum += lst[i][j]
            sum_dp += [i][n-1-i]
        if (sum_colum != sum_all) or (sum_dp != sum_all) or (sum_raw != sum_all):
            flag = False
            break

    sum_dg = 0
    for i in range(n):
        sum_dg += lst[i][i]
    if sum_dg != sum_all:
        flag = False

if flag: print('YES')
else: print('NO')