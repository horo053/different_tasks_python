#10.1. Попросите пользователя ввести две даты в формате год-месяц-день. Определите, сколько дней между введенными датами.
import datetime
def countDay(one_day,two_day):
    one_day = datetime.datetime.strptime(one_day, '%Y-%m-%d')
    two_day = datetime.datetime.strptime(two_day, '%Y-%m-%d')
    if one_day < two_day: print((two_day - one_day).days)
    elif one_day > two_day: print((one_day - two_day).days)
    else: print("Указан один день")

#one_day = input("Введите первую дату: ")
#two_day = input("Введите вторую дату: ")
#countDay(one_day,two_day)


#10.2. Заполните список случайными числами из промежутка от 1 до 100.
from random import randint
def randomIntList(length):
    lst = []
    for i in range(0, length):
        lst.append(randint(1,100))
    print(lst)

length = 10
randomIntList(length)


#10.3. Напишите программу, которая сформирует следующую строку: '12 34 56 78'
def format_number():
    numbers = [12, 34, 56, 78]
    result = ' '.join(map(str, numbers))
    print(result)

format_number()


# 10.4. Дан список с числами: [1, 2, 3, 3, 4, 5]. Проверьте, что в этом списке есть два одинаковых элемента подряд.
def intTwo(lst):
    n = 0
    k = 0
    for i in lst:
        if n == i:
            k += 1
            n = i
        else:
            n = i
    if k > 0: print("В списке есть два одинаковых числа")
    else: print("В списке нет двух одинаковых чисел")


lst = [1, 2, 3, 3, 4, 5]
intTwo(lst)