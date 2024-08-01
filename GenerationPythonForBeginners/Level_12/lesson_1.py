# 1. На вход программе подается четное число n≥2. Напишите программу, которая выводит список четных чисел [2, 4, 6, ..., n].
n = int(input())
lst = [i for i in range(1, n+1) if i%2 == 0]
print(lst)


# 2. На вход программе подаются две строки текста, содержащие целые числа. Из данных строк формируются списки чисел L и M.
# Напишите программу, которая создает третий список, элементами которого являются суммы соответствующих элементов списков L и M.
# Далее программа должна вывести каждый элемент полученного списка на одной строке через 1 пробел.
l = list(map(int, input().split()))
m = list(map(int, input().split()))
lst = [l[i]+m[i] for i in range(len(l))]
print(*lst)


# 3. На вход программе подается строка текста, содержащая натуральные числа. Напишите программу,
# которая вставляет между каждым числом знак +, а затем вычисляет сумму полученных чисел.
n = list(map(int, input().split()))
for ind, it in enumerate(n):
    if ind == len(n)-1:
        print(it, end='')
    else:
        print(f"{it}+", end='')
print(f"={sum(n)}")


# 4. На вход программе подается строка текста. Напишите программу, которая определяет, является ли введенная
# строка корректным телефонным номером. Строка текста является корректным телефонным номером, если она имеет формат:
# abc-def-hijk или 7-abc-def-hijk, где a, b, c, d, e, f, h, i, j, k – цифры от 0 до 9.
n = input()
if len(n) == 12:
    if n[3] == '-' and n[7] == '-':
        n = n.replace('-', '')
        if n.isdigit():
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
elif len(n) == 14:
    if n[1] == '-' and n[5] == '-' and n[9] == '-' and n[0] == '7':
        n = n.replace('-', '')
        if n.isdigit():
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
else:
    print('NO')


# 5. На вход программе подается строка текста. Напишите программу, использующую списочное выражение,
# которая находит длину самого длинного слова.
n = input().split()
l = 0
for i in n:
    if len(i) > l:
        l = len(i)
print(l)


# 6. На вход программе подается строка текста. Напишите программу, использующую списочное выражение,
# которая преобразует каждое слово введенного текста в "молодежный жаргон" по следующему правилу:
# первая буква каждого слова удаляется и ставится в конец слова;
# затем в конец слова добавляется слог "ки".
n = input().split()
lst = []
for i in n:
    s = i[1:]+i[0]+'ки'
    lst.append(s)
print(*lst)