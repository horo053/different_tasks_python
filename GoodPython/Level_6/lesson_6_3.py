import sys
#3. Объявите в программе следующий кортеж: t = (3.4, -56.7)
# На вход программе подается последовательность целых чисел, записанных через пробел.
# Необходимо их прочитать и добавить в конец кортежа t.
# Добавленные числа в кортеже должны следовать в порядке их считывания. Результат вывести на экран командой: print(t)
t = (3.4, -56.7)
inp_t = tuple(map(int, input().split()))
print(t + inp_t)


#4. На вход программе подается строка с названиями городов, записанных через пробел.
# Необходимо прочитать эту строку и на ее основе сформировать кортеж из названий городов.
# Названия в кортеже должны идти в том же порядке, что и в исходной строке.
# Выполните проверку: если в полученном кортеже нет города "Москва", то следует его добавить в конец кортежа.
# Выведите на экран названия городов из кортежа (по порядку) в одну строчку через пробел.
str_city = tuple(input().split())
t_city = ('Москва',)
if 'Москва' not in str_city:
    print(*str_city + t_city)
else:
    print(*str_city)


#5. На вход программе подается строка с названиями городов, записанных через пробел.
# Необходимо прочитать эту строку и на ее основе сформировать кортеж из названий городов.
# Затем, выполните проверку: если в полученном кортеже присутствует город "Ульяновск",
# то этот элемент следует удалить (создав новый кортеж).
# Выведите на экран названия городов из итогового кортежа (по порядку) в одну строчку через пробел.
city_t = tuple(input().split())
if 'Ульяновск' in city_t:
    city_t = city_t[:city_t.index('Ульяновск')] + city_t[city_t.index('Ульяновск')+1:]
print(*city_t)


#6. На вход программе подается строка с именами студентов, записанных через пробел.
# Необходимо прочитать эту строку и на ее основе сформировать кортеж из имен.
# Затем, отобразите на экране все имена из этого кортежа (по порядку), которые содержат фрагмент "ва" (без учета регистра).
# Имена выводятся в одну строчку через пробел в нижнем регистре (малыми буквами).
name_t = tuple(input().lower().split())
t_n = tuple()
for i in name_t:
    if "ва" in i:
        t_n += i,
print(*t_n)


#7. На вход программе подаются целые числа, записанные в одну строку через пробел.
# Необходимо их прочитать и сохранить в кортеже. Затем, создать еще один кортеж с уникальными (не повторяющимися)
# значениями из первого кортежа. Уникальные числа должны следовать в том же порядке, что и в исходном кортеже.
# Отобразите найденные уникальные числа в одну строчку через пробел.
# P. S. Подобные задачи решаются, как правило, с помощью множеств, но в качестве практики пока обойдемся без них.
t_inp = tuple(map(int, input().split()))
t_number = ()
for i in t_inp:
    if i not in t_number:
        t_number += i,
print(*t_number)


#8. На вход программе подаются целые числа, записанные в одну строку через пробел.
# Необходимо их прочитать и сохранить в кортеже. Затем, в кортеже найти и вывести в одну строчку через
# пробел (по порядку) все индексы неуникальных (повторяющихся) значений.
tp_inp = tuple(map(int, input().split()))
lst = []
for ind, it in enumerate(tp_inp):
    if tp_inp.count(it) > 1:
        lst.append(ind)
print(*lst)


#9. Объявите в программе следующий двумерный кортеж, размером 5 x 5 элементов
# На вход программе подается натуральное число N (N < 5). Необходимо на основе кортежа t сформировать новый аналогичный
# кортеж t2 размером N x N элементов путем отбрасывания последних строк и столбцов.
# Результат выведите на экран в виде таблицы чисел.
# P.S. Обратите внимание, что в при выводе таблицы в конце строк не должно быть пробелов.
t = ((1, 0, 0, 0, 0),
     (0, 1, 0, 0, 0),
     (0, 0, 1, 0, 0),
     (0, 0, 0, 1, 0),
     (0, 0, 0, 0, 1))
n = int(input())
t2 = ()
for i in t[:n]:
    print(*i[:n])


#10. На вход программе подаются строки (пункты меню), каждая с новой строки, в формате:
# название_1 URL-адрес_1
# название_2 URL-адрес_2
# ...
# название_N URL-адрес_N
# В программе уже реализовано чтение этих строк и сохранение их в списке: lst_in = list(map(str.strip, sys.stdin.readlines()))
# Необходимо преобразовать список lst_in так, чтобы получился кортеж menu следующего вида:
# ((название_1, URL-адрес_1), (название_2, URL-адрес_2), ... (название_N, URL-адрес_N))
# Полученный кортеж вывести на экран командой: print(menu)
lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_menu = []
for i in lst_in:
    lst_menu.append(tuple(i.split(),))
menu = tuple(lst_menu)
print(menu)