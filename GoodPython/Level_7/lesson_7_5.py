#2. Объявите в программе функцию с именем get_even, которая способна принимать произвольное количество чисел
# в качестве аргументов. Например: get_even(1, 2, 3, -5, 10, 8)
# Функция должна возвращать список, составленный только из четных переданных ей значений.
# P.S. Функцию вызывать не нужно, только определить.
def get_even(*args):
    lst = []
    for i in args:
        if i % 2 == 0:
            lst.append(i)
    return lst


#3. Объявите в программе функцию с именем get_biggest_city, которой можно передавать произвольное количество
# названий городов (строк) через аргументы. Например: get_biggest_city('Город 1', 'Город 2', 'Город 3', 'Город 4')
# Данная функция должна возвращать название города (строку) наибольшей длины. Если таких городов несколько,
# то первый переданный (из наибольших). Программу реализовать без использования сортировки.
# P.S. Функцию выполнять не нужно, только определить.
def get_biggest_city(*args):
    max = ''
    for i in args:
        if len(i) <= len(max):
            max = max
        else:
            max = i
    return max


#4. Объявите в программе функцию с именем get_data_fig для вычисления периметра произвольного N-угольника.
# На вход этой функции передаются N длин сторон через ее аргументы. Дополнительно могут быть указаны именованные аргументы:
# tp - булево значение True/False;
# color - целое числовое значение;
# closed - булево значение True/False;
# width - целое значение.
# Функция должна возвращать в виде кортежа периметр многоугольника и указанные значения именованных параметров в
# порядке их перечисления в тексте задания (если они были переданы). Если какой-либо параметр отсутствует,
# его возвращать не нужно (пропустить). P.S. Функцию выполнять не нужно, только объявить.
# def get_data_fig(*args, **kwargs):
#     sum_a = sum(args)
#     lst_k = []
#     for key in kwargs:
#         lst_k.append(kwargs.get(key))
#         return (sum_a, *lst_k)
