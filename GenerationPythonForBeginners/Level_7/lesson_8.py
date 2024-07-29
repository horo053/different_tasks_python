# 1. Дано натуральное число n (n≤ 9). Напишите программу, которая печатает таблицу размером n×3,
# состоящую из данного числа (числа отделены одним пробелом).
n = int(input())
for i in range(n):
    for j in range(3):
        print(n, end = ' ')
    print()


# 2. Дано натуральное число n (n≤ 9). Напишите программу, которая печатает таблицу размером n×5,
# где в i-ой строке указано число i (числа отделены одним пробелом).
n = int(input())
for i in range(1, n+1):
    for j in range(5):
        print(i, end = ' ')
    print()


# 3. Дано натуральное число n (n≤ 9). Напишите программу, которая печатает таблицу сложения для всех чисел
# от 1 до n (включительно) в соответствии с примером.
n = int(input())
for i in range(1, n+1):
    for j in range(1, 10):
        print(i, '+', j, '=', i+j)
    print()


# 4. Дано нечетное натуральное число n. Напишите программу, которая печатает равнобедренный звездный
# треугольник с основанием, равным n в соответствии с примером:*
# **
# ***
# ****
# ***
# **
# *
n = int(input())
for i in range(1, n + 1):
    print('*' * min(i, n - i + 1))


# Дано натуральное число n. Напишите программу, которая печатает численный треугольник в соответствии с примером:
# 1
# 22
# 333
# 4444
# 55555
# ...
n = int(input())
for i in range(1, n+1):
    for j in range(i):
        print(i, end='')
    print()