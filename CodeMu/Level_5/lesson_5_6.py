#6.1. Попросите пользователя ввести свой email. Проверьте, ввел ли он корректное значение.
import re
def emailTrue(email):
    pattern = re.compile(r"^\S+@\S+\.\S+$")
    is_valid = pattern.match(email)
    print(is_valid is not None)

#email = input("Введите свой email: ")
#emailTrue(email)


#6.2. Попросите пользователя ввести дату в формате год-месяц-день. Определите, была уже дата в текущем году.
import datetime
def datePastTrue(date_past):
    try:
        if datetime.datetime.strptime(date_past, '%Y-%m-%d').date() < datetime.date.today(): print("Дата прошла")
        elif datetime.datetime.strptime(date_past, '%Y-%m-%d').date() > datetime.date.today(): print("Будущая дата")
        elif datetime.datetime.strptime(date_past, '%Y-%m-%d').date() == datetime.date.today(): print("Текущая дата")
    except: print("Не дата")

#date_past = input("Введите дату: ")
#datePastTrue(date_past)


#6.3. Дан некоторый список, например, вот такой: [123, 456, 789]
# Слейте все элементы этого списка в один список, разбив их посимвольно: [1, 2, 3, 4, 5, 6, 7, 8, 9]
import datetime
def joinListInList(lst):
    lst1 = list(map(str,lst))
    lst2 = []
    for i in lst1:
        for j in i:
            lst2.append(j)
    print(list(map(int,lst2)))

lst = [123, 456, 789]
joinListInList(lst)