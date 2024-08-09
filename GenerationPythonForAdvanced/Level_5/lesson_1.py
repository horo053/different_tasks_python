# 1. На вход программе подается строка текста, содержащая символы и число n. Из данной строки формируется список.
# Напишите программу, которая разделяет список на вложенные подсписки так, что n последовательных элементов принадлежат разным подспискам.
s = input().split()
n = int(input())
lst = [[]*n for i in range(n)]
for i in range(n):
    for j in range(i, len(s), n):
        lst[i].append(s[j])
print(lst)


# 2. Напишите программу, которая выводит максимальный элемент в заштрихованной области квадратной матрицы:
# 0 0 1
# 0 1 1
# 1 1 1
n = int(input())
lst = [[int(i) for i in input().split()] for _ in range(n)]
max = 0
for i in range(n):
    for j in range(n):
        if ((i >= j or i <= j) and i > n-1-j) or (j == n-i-1):
            if lst[i][j] > max:
                max = lst[i][j]
print(max)


# 3. Напишите программу, которая транспонирует квадратную матрицу. Транспонированная матрица — матрица,
# полученная из исходной матрицы заменой строк на столбцы.
n = int(input())
lst = [[int(i) for i in input().split()] for _ in range(n)]
for i in range(n):
    for j in range(n):
        print(lst[j][i], end=' ')
    print()


# 4. На вход программе подается нечетное натуральное число n. Напишите программу, которая создает матрицу размером n×n
# заполнив её символами ".". Затем заполните символами * среднюю строку и столбец матрицы, главную и побочную диагональ
# матрицы. Выведите полученную матрицу на экран, разделяя элементы пробелами.
n = int(input())
lst = [['.' for i in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if (i==j) or (n == i+j+1) or (n//2 == j) or (n//2 == i):
            lst[i][j] = '*'
for i in lst:
    print(*i)

# ИЛИ:

n = int(input())
lst = [['*' if (i==j) or (n == i+j+1) or (n//2 == j) or (n//2 == i) else '.' for i in range(n)] for j in range(n)]
for i in lst:
    print(*i)


# 5. Напишите программу проверки симметричности квадратной матрицы относительно побочной диагонали.
n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
flag = True
for i in range(n):
    lst[i].reverse()
for i in range(n):
    for j in range(n):
        if lst[i][j] != lst[j][i]:
            flag = False
            break
if flag: print('YES')
else: print('NO')


# 6. Латинским квадратом порядка n называется квадратная матрица размером n×n, каждая строка и каждый столбец которой
# содержат все числа от 1 до n. Напишите программу, которая проверяет, является ли заданная квадратная матрица
# латинским квадратом. (--)
n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
for i in range(n):
    if sorted(matrix[i]) != list(range(1, n + 1)) or sorted([matrix[j][i] for j in range(n)]) != list(range(1, n + 1)):
        print('NO')
        break
else:
    print('YES')


# 7. На шахматной доске 8×8 стоит ферзь. Отметьте положение ферзя на доске и все клетки, которые бьет ферзь.
# Клетку, где стоит ферзь, отметьте буквой Q, клетки, которые бьет ферзь, отметьте символами *,
# остальные клетки заполните точками. (--)
x, y = input()
n = 8
board = [['.'] * n for _ in range(n)]
x = ord(x) - 97
y = n - int(y)

for i in range(n):
    for j in range(n):
        if i == y or j == x:
            board[i][j] = '*'
        elif abs(i - y) == abs(j - x):
            board[i][j] = '*'

board[y][x] = 'Q'

for row in board:
    print(*row)


# 8. На вход программе подается натуральное число n. Напишите программу, которая создает матрицу размером n×n и
# заполняет её по следующему правилу:
# на главной диагонали на месте каждого элемента должно стоять число 0;
# на двух диагоналях, прилегающих к главной, – число 1;
# на следующих двух диагоналях – число 2, и т.д. (--)
n = int(input())
lst = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            lst[i][j] = 0
        else:
            lst[i][j] = abs(j-i)
for i in lst:
    print(*i)