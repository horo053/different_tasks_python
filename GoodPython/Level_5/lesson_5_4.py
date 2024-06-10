#1. На вход программе подается строка. Необходимо ее прочитать и найти в ней все индексы строкового фрагмента "ра".
# Выведите найденные индексы на экран в одну строчку через пробел. Если же фрагмент "ра" отсутствует в строке, то вывести -1.
str1 = input()
ind = []
for i in range(len(str1)-1):
    if str1[i] == 'р' and str1[i+1] == 'а':
        ind.append(i)
if len(ind) > 0: print(*ind)
else: print(-1)


#2. На вход программе подается строка с номером телефона. Ожидается следующий формат номера в строке: +7(xxx)xxx-xx-xx
# где x - это любая цифра. Число введенных символов считается верным
# (то есть, не может быть, чтобы отсутствовала какая-либо цифра или была лишняя).
# Необходимо прочитать строку из входного потока и проверить, что она содержит номер телефона в соответствии
# с приведенным форматом. Вывести "ДА", если это так и "НЕТ" в противном случае.
phone = input()
str_int = '0123456789'
res = 0
if phone[0] == '+' and phone[1] == '7' and phone[2] == '(' and phone[6] == ")" and phone[10] == "-" and phone[13] == "-":
    phone = phone.replace('-', '')
    phone = phone.replace('(', '')
    phone = phone.replace(')', '')
    for i in range(2, len(phone)-1):
        if phone[i] in str_int:
            res += 1
        else:
            res += 0
if res == len(phone)-3: print("ДА")
else: print("НЕТ")


#3. На вход программе подается подается строка, в которой записано арифметическое выражение.
# Например: "10 + 25 - 12" или "10 + 25 - 12 + 20 - 1 + 3" и т. д. То есть, количество действий может быть произвольным.
# Необходимо прочитать эту строку из входного потока и выполнить вычисление, записанного в ней арифметического выражения.
# Результат вычисления отобразить на экране. Полагается, что в качестве арифметических операций используется
# только сложение (+) и вычитание (-), а в качестве операндов только целые неотрицательные числа.
# Следует учесть, что математические операции могут быть записаны как с пробелами (до и после), так и без них.
# P.S. В целях обучения программу следует делать без использования функции eval.
str1 = input().replace(" ", '')
str1 = str1.replace("+", " ")
str1 = str1.replace("-", " -")
lst = list(map(int, str1.split()))
sum = 0
for i in lst:
    sum += i
print(sum)


#4. На вход программе подаются целые числа, записанные в одну строку через пробел.
# Необходимо прочитать эти числа и сохранить в списке. Затем, каждое значение этого списка изменить
# на квадрат соответствующего числа. Результат (список) выведите на экран в виде последовательности чисел,
# записанных через пробел. Программу следует реализовать с использованием функции enumerate.
lst1 = list(map(int, input().split()))
for index, item in enumerate(lst1):
    lst1[index] = item ** 2
print(*lst1)


#5. На вход программе подаются целые числа, записанные в одну строку через пробел.
# Необходимо прочитать эти числа и сохранить в списке. Затем, каждый элемент этого списка продублировать один раз.
# Например, для списка: [1, 2, 3] после дублирования должны получить: [1, 1, 2, 2, 3, 3]
# Результат (список) выведите на экран в виде последовательности чисел, записанных через пробел.
lst2 = list(map(int, input().split()))
new_list = []
for i in range(len(lst2)):
    new_list.append(lst2[i])
    new_list.append(lst2[i])
print(*new_list)


#6. На вход программе подаются вещественные числа, записанные через пробел.
# Необходимо прочитать эти числа и сохранить в списке. Затем, с помощью цикла for нужно найти
# наименьшее число в этом списке. Полученный результат (минимальное число) вывести на экран.
# Реализовать программу без использования функции min, max и сортировки.
lst3 = list(map(float, input().split()))
min = lst3[0]
for i in range(1, len(lst3)):
    if lst3[i] < min: min = lst3[i]
print(min)


#7. На вход программе подаются вещественные числа, записанные через пробел.
# Необходимо прочитать эти числа и сохранить в списке. Затем, все отрицательные значения в этом списке заменить на -1.0.
# Результат (список) выведите на экран в виде последовательности чисел, записанных через пробел.
# Программу следует реализовать с использованием функции enumerate.
lst4 = list(map(float, input().split()))
for index, item in enumerate(lst4):
    if item < 0: lst4[index] = -1.0
print(*lst4)