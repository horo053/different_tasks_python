# 1. Напишите функцию get_middle_point(x1, y1, x2, y2), которая принимает в качестве аргументов координаты концов отрезка
# (x1: y1) и (x2; y2) и возвращает координаты точки являющейся серединой данного отрезка.
def get_middle_point(x1, y1, x2, y2):
    z1 = (x1 + x2) / 2
    z2 = (y1 + y2) / 2
    return z1, z2

x_1, y_1 = int(input()), int(input())
x_2, y_2 = int(input()), int(input())

x, y = get_middle_point(x_1, y_1, x_2, y_2)
print(x, y)


# 2. Напишите функцию get_circle(radius), которая принимает в качестве аргумента радиус окружности и возвращает
# два значения: длину окружности и площадь круга, ограниченного данной окружностью.
import math
def get_circle(radius):
    C = 2 * math.pi * radius
    S = math.pi * radius**2
    return C, S

r = float(input())

length, square = get_circle(r)
print(length, square)


# 3. Напишите функцию solve(a, b, c), которая принимает в качестве аргументов три целых числа
# a, b, c – коэффициенты квадратного уравнения ax**2+bx+c=0 и возвращает его корни в порядке возрастания.
# объявление функции
def solve(a, b, c):
    D = b ** 2 - 4 * a * c
    x1 = (-b - D ** 0.5) / (2 * a)
    x2 = (-b + D ** 0.5) / (2 * a)
    return min(x1, x2), max(x1, x2)

a, b, c = int(input()), int(input()), int(input())

x1, x2 = solve(a, b, c)
print(x1, x2)