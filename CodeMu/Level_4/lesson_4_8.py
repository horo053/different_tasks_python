#8.1. Сформируйте с помощью циклов следующий список: [ ['x', 'x', 'x'], ['x', 'x', 'x'], ['x', 'x', 'x'], ]
def listCyrcle(stroka,stolb):
    lst_big = []

    for i in range(stroka):
        lst_small = []
        for j in range(stolb):
            lst_small.append('x')
        lst_big.append(lst_small)
    print(lst_big)

stroka, stolb = 3,3
listCyrcle(stroka,stolb)


print()
#8.2. Сформируйте с помощью циклов следующий список:
def listCyrcleTree(stroka1,stolb1):
    lst_big = []
    for i in range(stroka1):
        lst_small = []
        for j in range(1,stolb1+1):
            lst_small.append(j)
        lst_big.append(lst_small)
    print(lst_big)

stroka1,stolb1 = 5,3
listCyrcleTree(stroka1,stolb1)


print()
#8.3. Дана строка:
def delNullStr(str1):
    list1 = str1.split()
    print('\n'.join(list1))

str1 = '''
	text1
	text2
	
	text3
	text4
	
	text5
'''
delNullStr(str1)