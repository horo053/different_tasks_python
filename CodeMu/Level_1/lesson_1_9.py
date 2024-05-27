#9.1. Дана строка: 'abcdef'. Получите три последних символа этой строки: 'def'
def threeLetter(list_str):
    print(list_str[3:])

list_str = 'abcdef'
threeLetter(list_str)


print()
#9.2. Дан словарь с числами: {'a': 1,'b': 2,'c': 3, 'd': 4}. Увеличьте каждое число из словаря в 2 раза
def dictValue(list_str):
    for key in list_str:
        list_str[key] *= 2
    print(list_str)

dict_int = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
dictValue(dict_int)