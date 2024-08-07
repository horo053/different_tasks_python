# 1. На вход программе подается число n. Напишите программу, которая создает и выводит построчно список, состоящий из
# n списков [[1, 2, ..., n], [1, 2, ..., n], ..., [1, 2, ..., n]].
n = int(input())
lst = []
s = 1
for i in range(n):
    lst = [j for j in range(1, n+1)]
    print(lst)


# 2. На вход программе подается число n. Напишите программу, которая создает и выводит построчно вложенный список,
# состоящий изn списков [[1], [1, 2], [1, 2, 3], ..., [1, 2, ..., n]].
n = int(input())
lst = []
s = 1
for i in range(1, n+1):
    lst.append(i)
    print(lst)


# 3. Треугольник Паскаля — бесконечная таблица биномиальных коэффициентов, имеющая треугольную форму. В этом
# треугольнике на вершине и по бокам стоят единицы. Каждое число равно сумме двух расположенных над ним чисел.
# На вход программе подается число n. Напишите программу, которая возвращает указанную строку треугольника
# Паскаля в виде списка (нумерация строк начинается с нуля).
n = int(input())
r = [1]
for i in range(n):
    r = [sum(i) for i in zip([0]+r, r+[0])]
print(r)


# 4. На вход программе подается натуральное число n. Напишите программу, которая выводит первые n строк треугольника Паскаля
n = int(input())
r = [1]
for i in range(n):
    print(*r)
    r = [sum(i) for i in zip([0]+r, r+[0])]


# 5. На вход программе подается строка текста, содержащая символы. Напишите программу, которая упаковывает
# последовательности одинаковых символов заданной строки в подсписки.
n = input().split()
ls = [[n[0]]]
for i in range(1, len(n)):
    if n[i] == n[i-1]:
        ls[-1].append(n[i])
    else:
        ls.append([n[i]])
print(ls)
