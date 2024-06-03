#7.1. Попросите пользователя ввести свой номер телефона. Проверьте, ввел ли он корректное значение.
import re
def phoneTrue(phone):
    pattern = re.compile(r"^\+\d{1}\(\d{3}\)-\d{2}-\d{2}$")
    is_valid = pattern.match(phone)
    print(is_valid is not None)

phone = input("Введите свой телефон: ")
phoneTrue(phone)


#7.2. Попросите пользователя ввести десять чисел.
# Сохраните полученные числа в список, а зате получите среднее арифметическое этих чисел и выведите результат.
def avgList(lst_int):
    avg = 0
    if len(lst_int) < 10:
        for i in lst_int:
            avg += i
        avg = avg / len(lst_int)
        print(avg)
    else: print("В списке больше 10 цифр")


lst_int = list(map(int, input("Введите десять чисел: ").split()))
avgList(lst_int)


#7.3. Выведите в консоль даты всех выходных дней текущего года в формате год-месяц-день.
import datetime
def weekendDayInYear():
    count = 0
    start_year = datetime.datetime.strptime("2024-01-01", '%Y-%m-%d')
    while start_year < datetime.datetime.today():
        if datetime.datetime.isoweekday(start_year) == 6 or datetime.datetime.isoweekday(start_year) == 7:
            count += 1
        start_year += datetime.timedelta(days=1)
    print(count)

weekendDayInYear()


#7.4. Дано некоторое число: 123456
# Найдите сумму пар цифр этого числа. В нашем случае имеется ввиду следующее: 12 + 34 + 56
import datetime
def sumInt(num):
    sum = 0
    str_num = str(num)
    lst_num = [int(str_num[i:i+2]) for i in range(0, len(str_num),2)]
    for i in lst_num:
        sum += i
    print(sum)

num = 123456
sumInt(num)

