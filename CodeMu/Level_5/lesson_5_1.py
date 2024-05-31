#1.1. Выведите текущую дату в формате год-месяц-день.
import datetime

print(datetime.date.today())


print()
#1.2. Попросите пользователя ввести число через консоль. В результате выведите квадратный корень этого числа.
def dayQtr(day):
    print(int(day)**0.5)

day = input("Введите число месяца: ")
dayQtr(day)


print()
#1.3. Напишите программу, которая сформирует следующую строку: 'xxxxx'
def generateListX(count):
    res = ''
    for i in range(count):
        res = res + 'x'
    print(res)

count = 5
generateListX(count)


print()
#1.4. Дана некоторая строка со словами: 'aaa bbb ccc eee fff'
# Удалите из этой строки каждое второе слово. В нашем случае должно получится следующее: 'aaa ccc fff'
def delElement(str):
    list_str = str.split(' ')
    for index, i in enumerate(list_str[::-1]):
        if index % 2 != 0: list_str.remove(i)
    print(' '.join(list_str))

str = 'aaa bbb ccc eee fff'
delElement(str)