# 1. На вход программе подаются два натуральных числа n и m, каждое на отдельной строке — количество строк и столбцов
# в матрице. Далее вводятся сами элементы матрицы — слова, каждое на отдельной строке; подряд идут элементы сначала
# первой строки, затем второй, и т.д. Напишите программу, которая сначала считывает элементы матрицы один за другим,
# затем выводит их в виде матрицы.
s = int(input())
c = int(input())
mat = [[input() for i in range(c)] for i in range(s)]
for i in range(s):
    for j in range(c):
        print(mat[i][j], end=' ')
    print()


# 2. На вход программе подаются два натуральных числа n и m, каждое на отдельной строке — количество строк и столбцов
# в матрице. Далее вводятся сами элементы матрицы — слова, каждое на отдельной строке; подряд идут элементы сначала
# первой строки, затем второй, и т.д. Напишите программу, которая считывает элементы матрицы один за другим,
# выводит их в виде матрицы, выводит пустую строку, и снова ту же матрицу, но уже поменяв местами строки со столбцами:
# первая строка выводится как первый столбец, и так далее.
s = int(input())
c = int(input())
mat = [[input() for i in range(c)] for i in range(s)]
for i in range(s):
    for j in range(c):
        print(mat[i][j], end=' ')
    print()
print()
for i in range(c):
    for j in range(s):
        print(mat[j][i], end=' ')
    print()


# 3. Следом квадратной матрицы называется сумма элементов главной диагонали.
# Напишите программу, которая выводит след заданной квадратной матрицы.
n = int(input())
mat = [list(map(int, input().split())) for i in range(n)]
sum = 0
for i in range(n):
    for j in range(n):
        if i == j:
            sum += mat[i][j]
print(sum)


# 4. Напишите программу, которая выводит количество элементов квадратной матрицы в каждой строке, больших среднего
# арифметического элементов данной строки.
n = int(input())
mat = [list(map(int, input().split())) for i in range(n)]
for i in range(n):
    count = 0
    for j in range(n):
        if mat[i][j] > sum(mat[i]) / n:
            count += 1
    print(count)


# 5. Напишите программу, которая выводит максимальный элемент в заштрихованной области квадратной матрицы.
# [1 0 0]
# [1 1 0]
# [1 1 1]
n = int(input())
mat = [list(map(int, input().split())) for i in range(n)]
m = mat[0][0]
for i in range(n):
    for j in range(n):
        if i >= j:
            if mat[i][j] > m:
                m = mat[i][j]
print(m)


# 6. Напишите программу, которая выводит максимальный элемент в заштрихованной области квадратной матрицы:
# [1 0 1]
# [1 1 1]
# [1 0 1]
n = int(input())
mat = [list(map(int, input().split())) for i in range(n)]
m = mat[0][0]
for i in range(n):
    for j in range(n):
        if (i == j) or (i > j and i < (n-1-j)) or (i < j and i > (n-1-j)) or ((i+j+1) == n):
            if mat[i][j] > m:
                m = mat[i][j]
print(m)


# 7. Квадратная матрица разбивается на четыре четверти, ограниченные главной и побочной диагоналями: верхнюю, нижнюю,
# левую и правую. Напишите программу, которая вычисляет сумму элементов: верхней четверти; правой четверти;
# нижней четверти; левой четверти. Примечание: Элементы диагоналей не учитываются.
n = int(input())
mat = [list(map(int, input().split())) for i in range(n)]
height = 0
right = 0
low = 0
left = 0
for i in range(n):
    for j in range(n):
        if (i < j) and (i < (n - 1 - j)):
            height += mat[i][j]
        if (i < j) and (i > (n - 1 - j)):
            right += mat[i][j]
        if (i > j) and (i > (n - 1 - j)):
            low += mat[i][j]
        if (i > j) and (i < (n - 1 - j)):
            left += mat[i][j]
print(f"Верхняя четверть: {height}")
print(f"Правая четверть: {right}")
print(f"Нижняя четверть: {low}")
print(f"Левая четверть: {left}")