# 1. Напишите функцию convert_to_miles(km), которая принимает в качестве аргумента расстояние в километрах и возвращает
# расстояние в милях. Формула для преобразования: мили = километры * 0.6214
def convert_to_miles(km):
    return km * 0.6214

num = int(input())

print(convert_to_miles(num))


# 2. Напишите функцию get_days(month), которая принимает в качестве аргумента номер месяца и возвращает количество дней в данном месяце.
# Примечание 1. Гарантируется, что передаваемый аргумент находится в диапазоне от 1 до 12.
# Примечание 2. Считайте, что год является невисокосным.
def get_days(month):
    if month in [1,3,5,7,8,10,12]:
        return 31
    elif month == 2:
        return 28
    else:
        return 30

num = int(input())

print(get_days(num))


# 3. Напишите функцию get_factors(num), принимающую в качестве аргумента натуральное число и возвращающую
# список всех делителей данного числа.
def get_factors(num):
    divisors = []
    for i in range(1, num+1):
        if num % i == 0:
            divisors.append(i)
    return divisors

n = int(input())

print(get_factors(n))


# 4. Напишите функцию number_of_factors(num), принимающую в качестве аргумента число и возвращающую количество делителей данного числа.
def number_of_factors(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    return count

n = int(input())

print(number_of_factors(n))


# 5. Напомним, что строковый метод find('a') возвращает местоположение первого вхождения символа a в строке.
# Проблема заключается в том, что данный метод не находит местоположение всех символов а.
# Напишите функцию с именем find_all(target, symbol), которая принимает два аргумента: строку target и символ symbol
# и возвращает список, содержащий все местоположения этого символа в строке.
# Примечание 1. Если указанный символ не встречается в строке, то следует вернуть пустой список.
def find_all(target, symbol):
    lst = []
    for ind, it in enumerate(target):
        if it == symbol:
            lst.append(ind)
    return lst

s = input()
char = input()

print(find_all(s, char))


# 6. Напишите функцию merge(list1, list2), которая принимает в качестве аргументов два отсортированных по
# возрастанию списка, состоящих из целых чисел, и объединяет их в один отсортированный список.
# Примечание 1. Списки list1 и list2 могут иметь разную длину.
def merge(list1, list2):
    lst = list1 + list2
    return sorted(lst)

numbers1 = [int(c) for c in input().split()]
numbers2 = [int(c) for c in input().split()]

print(merge(numbers1, numbers2))


# 7. На вход программе подается число n, а затем n строк, содержащих целые числа в порядке возрастания.
# Из данных строк формируются списки чисел. Напишите программу, которая объединяет указанные списки в один
# отсортированный список с помощью функции quick_merge(), а затем выводит его.
def quick_merge(lst1, lst2):
    res = []
    p1, p2 = 0, 0
    while p1 < len(lst1) and p2 < len(lst2):
        if lst1[p1] < lst2[p2]:
            res.append(lst1[p1])
            p1 += 1
        else:
            res.append(lst2[p2])
            p2 += 1
    if p1 == len(lst1):
        res += lst2[p2:]
    else:
        res += lst1[p1:]
    return res
res = []
for _ in range(int(input())):
    num = [int(c) for c in input().split()]
    res = quick_merge(res, num)
print(*res)
