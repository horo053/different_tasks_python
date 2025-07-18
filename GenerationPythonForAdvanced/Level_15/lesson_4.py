# 1. Напишите программу, которая с помощью функции map() округляет все элементы списка numbers до 2
# десятичных знаков, а затем выводит их, каждый на отдельной строке.
def map(function, items):
    result = []
    for item in items:
        result.append(function(item,2))
    return result


numbers = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.12013, 23.22222, 90.09873, 45.45, 314.1528, 2.71828, 1.41546]

print(*map(round, numbers), sep='\n')


# 2. Напишите программу, которая с помощью функций filter() и map() отбирает из заданного списка numbers трехзначные
# числа, дающие при делении на 5 остаток 2, и выводит их кубы, каждый на отдельной строке.
# Примечание. Остаток 2 при делении на 5 должно давать само число, а не его куб.
def map(function, items):
    result = []
    for item in items:
        result.append(function(item**3))
    return result


def filter(function, items):
    result = []
    for item in items:
        if function(item):
            result.append(item)
    return result


numbers = [1014, 1321, 675, 1215, 56, 1386, 1385, 431, 1058, 486, 1434, 696, 1016, 1084, 424, 1189, 475, 95, 1434,
           1462, 815, 776, 657, 1225, 912, 537, 1478, 1176, 544, 488, 668, 944, 207, 266, 1309, 1027, 257, 1374, 1289,
           1155, 230, 866, 708, 144, 1434, 1163, 345, 394, 560, 338, 232, 182, 1438, 1127, 928, 1309, 98, 530, 1013,
           898, 669, 105, 130, 1363, 947, 72, 1278, 166, 904, 349, 831, 1207, 1496, 370, 725, 926, 175, 959, 1282, 336,
           1268, 351, 1439, 186, 273, 1008, 231, 138, 142, 433, 456, 1268, 1018, 1274, 387, 120, 340, 963, 832, 1127]

def fil(x):
    return len(str(x)) == 3 and x%5 == 2

def cube(x):
    return x**3

filt = filter(fil, numbers)
print(*map(cube, filt), sep='\n')


# 3. Напишите программу для вычисления и вывода суммы квадратов элементов списка numbers.
# Примечание. Попробуйте решить задачу двумя способами: с помощью функции reduce() и с помощью функций map() и sum().
def reduce(operation, items, initial_value):
    acc = initial_value
    for item in items:
        acc = operation(acc, item**2)
    return acc


numbers = [97, 42, 9, 32, 3, 45, 31, 77, -1, 11, -2, 75, 5, 51, 34, 28, 46, 1, -8, 84, 16, 51, 90, 56, 65, 90, 23,
           35, 11, -10, 70, 90, 90, 12, 96, 58, -8, -4, 91, 76, 94, 60, 72, 43, 4, -6, -5, 51, 58, 60, 30, 38, 67,
           62, 36, 72, 34, 82, 62, -1, 60, 82, 87, 81, -7, 57, 26, 36, 17, 43, 80, 40, 75, 94, 91, 64, 38, 72, 29,
           84, 38, 35, 7, 54, 31, 95, 78, 27, 82, 1, 64, 94, 31, 29, -8, 98, 24, 61, 7, 73]

def add(x, y):
    return x+y

total = reduce(add, numbers, 0)
print(total)


# 4. Напишите программу для вычисления и вывода суммы квадратов двузначных чисел из списка numbers,
# которые делятся на 7 без остатка.
# Примечание 1. При решении задачи используйте функции filter(), map() и sum().
# Примечание 2. На 7 должно делиться исходное двузначное число, а не его квадрат.
# Примечание 3. Не забывайте про отрицательные двузначные числа.
def map(function, items):
    result = []
    for item in items:
        result.append(function(item))
    return result


def filter(function, items):
    result = []
    for item in items:
        if function(item):
            result.append(item)
    return result


numbers = [77, 293, 28, 242, 213, 285, 71, 286, 144, 276, 61, 298, 280, 214, 156, 227, 228, 51, -4, 202, 58, 99,
           270, 219, 94, 253, 53, 235, 9, 158, 49, 183, 166, 205, 183, 266, 180, 6, 279, 200, 208, 231, 178, 201,
           260, -35, 152, 115, 79, 284, 181, 92, 286, 98, 271, 259, 258, 196, -8, 43, 2, 128, 143, 43, 297, 229,
           60, 254, -9, 5, 187, 220, -8, 111, 285, 5, 263, 187, 192, -9, 268, -9, 23, 71, 135, 7, -161, 65, 135,
           29, 148, 242, 33, 35, 211, 5, 161, 46, 159, 23, 169, 23, 172, 184, -7, 228, 129, 274, 73, 197, 272, 54,
           278, 26, 280, 13, 171, 2, 79, -2, 183, 10, 236, 276, 4, 29, -10, 41, 269, 94, 279, 129, 39, 92, -63, 263,
           219, 57, 18, 236, 291, 234, 10, 250, 0, 64, 172, 216, 30, 15, 229, 205, 123, -105]

def fil(x):
    return (9 < abs(x) < 100) and x % 7 == 0

def kv(x):
    return x**2

filt = filter(fil, numbers)
res = map(kv, filt)
print(sum(res))
print(sum(map(kv, filter(fil, numbers))))


# 5. Напишите функцию func_apply(), принимающую на вход функцию и список значений и возвращающую список,
# в котором каждое значение будет результатом применения переданной функции к переданному списку.
def func_apply(function, items):
    result = []
    for item in items:
        result.append(function(item))
    return result

def add3(x):
    return x + 3


def mul7(x):
    return x * 7


print(func_apply(mul7, [1, 2, 3, 4, 5, 6]))
print(func_apply(add3, [1, 2, 3, 4, 5, 6]))
print(func_apply(str, [1, 2, 3, 4, 5, 6]))