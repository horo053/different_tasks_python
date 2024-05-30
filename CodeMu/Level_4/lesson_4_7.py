#7.1. Дан список со числами. Проверьте, что в нем есть число, содержащее в себе цифру 3.
def listHaveThree(lst_have_three):
    str_list = [str(item) for item in lst_have_three]
    count = 0
    for i in str_list:
        if '3' in i: count += 1
    if count > 0: print('В списке есть число с тройкой')
    else: print('В списке нет числа с тройкой')


lst1,lst2 = [1,345,87954], [256,7567,1041]
listHaveThree(lst1)
listHaveThree(lst2)


print()
#7.2. Дана следующая структура: lst = [ { 1: (1, 2, 3), 2: (1, 2, 3), 3: (1, 2, 3), }, { 1: (1, 2, 3), 2: (1, 2, 3), 3: (1, 2, 3), }, { 1: (1, 2, 3), 2: (1, 2, 3), 3: (1, 2, 3), }, ];
# Найдите сумму элементов этой структуры.
def sumElement(lst):
    sum = 0
    for i in lst:
        for j in i.values():
            for l in j:
                sum += l
    print(sum)


lst = [
	{
		1: (1, 2, 3),
		2: (1, 2, 3),
		3: (1, 2, 3),
	},
	{
		1: (1, 2, 3),
		2: (1, 2, 3),
		3: (1, 2, 3),
	},
	{
		1: (1, 2, 3),
		2: (1, 2, 3),
		3: (1, 2, 3),
	},
];
sumElement(lst)


print()
#7.3. Дан список: ['text1','text2','text3','text4','text5',]
# Сделайте из этого списка строку так, чтобы каждый элемент списка был на новой линии: '''text1text2text3text4text5'''
def listInStr(lst3):
    str1 = '\n'.join(lst3)
    print(str1)


lst3 = [
	'text1',
	'text2',
	'text3',
	'text4',
	'text5',
]
listInStr(lst3)