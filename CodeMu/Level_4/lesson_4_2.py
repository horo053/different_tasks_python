#2.1. Дано число. Получите список делителей этого числа.
def countDiv(int1):
    count = 0
    for i in range(1,10):
        if int1 % i == 0: count += 1
    print(f"У числа {int1} - {count} делителей")

int1 = 124536
countDiv(int1)


print()
#2.2. Выведите в консоль все числа в промежутке от 10 до 1000, у которых первая цифра четная.
def сhetOneInt(range_int):
    list_int = []
    for i in range(1,range_int+1):
        rev_i = str(i)[::-1]
        int_rev_i = int(rev_i)
        if (int_rev_i % 10) % 2 == 0: list_int.append(i)
    print(list_int)

range_int = 1000
сhetOneInt(range_int)


print()
#2.3. Дан список: [ [1, 2, 3], [4, 5, 6], [7, 8, 9], ]. Найдите сумму элементов этого списка.
def sumElementList(str1):
    sum = 0
    for i in str1:
        for j in i:
            sum += j
    print(sum)

str1 = [ [1, 2, 3], [4, 5, 6], [7, 8, 9], ]
sumElementList(str1)


print()
#2.4. Дан следующий словарь: dct = { 1: { 1: 11, 2: 12, 3: 13, }, 2: { 1: 21, 2: 22, 3: 23, }, 3: { 1: 24, 2: 25, 3: 26, }, }
# Найдите сумму элементов этого словаря.
def sumElementDict(dct):
    sum = 0
    for i in dct.values():
        for j in list(i.values()):
            sum += j
    print(sum)

dct = { 1: { 1: 11, 2: 12, 3: 13, },
                2: { 1: 21, 2: 22, 3: 23, },
                3: { 1: 24, 2: 25, 3: 26, }, }
sumElementDict(dct)