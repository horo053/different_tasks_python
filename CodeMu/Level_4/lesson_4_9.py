#9.1. Сформируйте с помощью циклов следующий список: [ [1, 2, 3], [4, 5, 6], [7, 8, 9], ]
def generateList(stroka,stolb):
    lst_big = []
    num = 1

    for i in range(stroka):
        lst_small = []
        for j in range(stolb):
            lst_small.append(num)
            num += 1
        lst_big.append(lst_small)
    print(lst_big)

stroka,stolb = 3,3
generateList(stroka,stolb)


print()
#9.2. Дан текст: '''a-1b-2c-3d-4e-5'''. Разбейте эту строку в словарь следующим образом: { 'a': 1 'b': 2 'c': 3 'd': 4 'e': 5 }
def strInDict(str):
    str_list = str.split()
    list_list = []
    dict_l = {}
    for i in str_list:
        list_list = i.split('-')
        dict_l.update(dict.fromkeys([list_list[0]], list_list[1]))
    print(dict_l)

str = '''
	a-1
	b-2
	c-3
	d-4
	e-5
'''
strInDict(str)