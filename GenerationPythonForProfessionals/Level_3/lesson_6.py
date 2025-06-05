import time
#1. Реализуйте функцию calculate_it(), которая принимает один или более аргументов в следующем порядке:
# func — произвольная функция
# *args — переменное количество позиционных аргументов, каждый из которых является произвольным объектом
# Функция должна возвращать кортеж, первым элементом которого является возвращаемое значение функции func при
# вызове с аргументами *args, а вторым — примерное время (в секундах), затраченное на вычисление этого значения.
def calculate_it(func, *args):
    start = time.time()
    res = func(*args)
    end = time.time()
    return res, end - start


#2. Реализуйте функцию get_the_fastest_func(), которая принимает два аргумента в следующем порядке:
# funcs — список произвольных функций
# arg — произвольный объект
# Функция get_the_fastest_func() должна возвращать функцию из списка funcs, которая затратила на вычисление
# значения при вызове с аргументом arg наименьшее количество времени.
def get_the_fastest_func(funcs, arg):
   times = []
   for func in funcs:
       starttime = time.time()
       func(arg)
       endtime = time.time()
       times.append(endtime - starttime)
   return funcs[times.index(min(times))]
