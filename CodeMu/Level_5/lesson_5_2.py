#2.1. Попросите пользователя ввести дату в формате год-месяц-день. Проверьте, ввел ли он корректное значение.
from datetime import datetime

def trueDate(date):
    try:
        datetime.strptime(date, "%Y-%m-%d").date()
        print("Соответсвует формату")
    except:
        print("Не соответсвует формату")

date = input("Введите дату в формате 'год-месяц-день': ")
trueDate(date)


print()
#2.2. Попросите пользователя ввести целое число через консоль. Проверьте, ввел ли он корректное значение.
from datetime import datetime
def trueInt(int1):
    try:
        int(int1) == float(int1)
        print("Целое число")
    except:
        print("Не целое число")

int1 = input("Введите целое число': ")
trueInt(int1)


print()
#2.3. Напишите программу, которая сформирует следующую строку: '12345'
from datetime import datetime
def generateStr(count):
    res = ''
    for i in range(1,count+1):
        res = res + str(i)
    print(res)

count = 5
generateStr(count)


print()
#2.4. Дан некоторый список, например, вот такой: [1, 2, 3, 4, 5, 6]
#По очереди выведите в консоль подсписки из двух элементов нашего списка: [1, 2] [3, 4] [5, 6]
def listInList(lst):
    for i in range(0, len(lst), 2):
        print(lst[i:i + 2])

lst = [1, 2, 3, 4, 5, 6]
listInList(lst)