#1. Объявите функцию с именем get_sq, которая вычисляет площадь прямоугольника по двум параметрам:
# width и height - ширина и высота прямоугольника, и возвращает результат (сама ничего на экран не выводит).
# То есть, функция имеет сигнатуру: def get_sq(width, height): ...
# Определите декоратор func_show для этой функции, который отображает результат на экране в виде строки (без кавычек):
# "Площадь прямоугольника: <значение>"
# Вызывать функцию и декоратор не нужно, только объявить. Применять декоратор к функции также не нужно.
def func_show(func):
    def func_sh(*args, **kwargs):
        res = func(*args, **kwargs)
        print(f"Площадь прямоугольника: {res}")
    return func_sh

def get_sq(width, height):
    return int(width) * int(height)

f = func_show(get_sq)


#2. На вход программы поступает строка с названиями пунктов меню, записанные в одну строчку через пробел.
# В программе реализовано чтение этой строки командой: menu = input()
# Необходимо задать функцию с именем get_menu с сигнатурой: def get_menu(s): ...
# которая преобразует переданную ей строку s в список из слов и возвращает этот список.
# Определите декоратор для этой функции с именем show_menu, который отображает список на экран в формате:
# 1. Пункт_1
# 2. Пункт_1
# ...
# N. Пункт_N
# Примените декоратор show_menu к функции get_menu, используя оператор @. Более ничего в программе делать не нужно.
# Сами функции не вызывать.
menu = input()
def show_menu(func):
    def show_menu_list(*args):
        res = func(*args)
        for ind, it in enumerate(res):
            print(f"{ind+1}. {it}")
    return show_menu_list

@show_menu
def get_menu(s=""):
    return list(s.split())


#3. На вход программы поступает строка из целых чисел, записанных через пробел.
# Необходимо прочитать эту строку и сохранить в какой-либо переменной. Напишите функцию get_list с одним параметром,
# которая преобразовывает эту строку в список из целых чисел и возвращает его.
# Определите декоратор для функции get_list, который сортирует список чисел по возрастанию.
# Результат сортировки должен возвращаться в виде списка чисел при вызове декоратора.
# Вызовите декорированную функцию get_list и отобразите полученный отсортированный список lst командой: print(*lst)
str1 = input()
def show_list(func):
    def show_menu_list(*args):
        res = sorted(func(*args))
        return res
    return show_menu_list
@show_list
def get_list(s=""):
    return [int(i) for i in s.split()]

print(*get_list(str1))


#4. На вход программе поступают две строки. В каждой строке записаны слова через пробел.
# Прочитайте эти строки и сохраните их в двух переменных. Объявите функцию с двумя параметрами,
# которой передаются строки со словами и преобразовываются в два списка из слов. Функция должна возвращать кортеж
# с этими списками в порядке: сначала первый список (первой строки), затем - второй.
# Определите декоратор для этой функции, который из двух списков формирует словарь, в котором ключами являются слова
# из первого списка, а значениями - соответствующие элементы из второго списка. Длины списков полагаются равными.
# Полученный словарь должен возвращаться при вызове декоратора. Примените декоратор к первой функции и вызовите
# ее для прочитанных строк. Результат (словарь d) отобразите на экране командой: print(*sorted(d.items()))
str_eng = input()
str_rus = input()
def show_dict(func):
    def show_menu_list(*args):
        res = list(func(*args))
        res = zip(res[0], res[1])
        return res
    return show_menu_list
@show_dict
def return_tuple(eng, rus):
    lst_eng = [int(i) for i in eng.split()]
    lst_rus = [int(i) for i in rus.split()]
    return lst_eng, lst_rus

print(*sorted(return_tuple(str_eng, str_rus)))


#ИЛИ
str_eng = input()
str_rus = input()
def show_dict(func):
    def show_menu_list(*args):
        res = list(func(*args))
        d = dict(zip(res[0], res[1]))
        return d
    return show_menu_list
@show_dict
def return_tuple(eng, rus):
    lst_eng = [i for i in eng.split()]
    lst_rus = [i for i in rus.split()]
    return lst_eng, lst_rus

d = return_tuple(str_eng, str_rus)
print(*sorted(d.items()))


#5.Объявите функцию, которая принимает строку с кириллицей и латиницей и преобразовывает русские символы в латиницу,
# используя следующий словарь для замены русских букв на соответствующее латинское написание:
# t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
#      'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
#      'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
#      'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
# Функция должна возвращать преобразованную строку. Замены делать без учета регистра (переданную строку перевести
# в нижний регистр - малые буквы). Небуквенные символы " : ;.,_" превращать в символ '-' (дефиса).
# Определите декоратор для этой функции, который несколько подряд идущих дефисов, превращает в один дефис.
# Полученная строка должна возвращаться при вызове декоратора. (Сам декоратор на экран ничего выводить не должен).
# Примените декоратор к первой функции и вызовите ее для строки s, прочитанной из входного потока командой: s = input()
t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
s = input()

def replace_hyphen(func):
    def hyphen_one(*args):
        res = func(*args)
        i = "--"
        for i in res:
            res = res.replace("--", "-")
        return res
    return hyphen_one

@replace_hyphen
def return_eng(str2='', t={}):
    str2 = str2.lower()
    for i in str2:
        if i in " : ;.,_":
            str2 = str2.replace(i, "-")
        for i in t:
            str2 = str2.replace(i, t.get(i))
    return str2

print(return_eng(s,t))