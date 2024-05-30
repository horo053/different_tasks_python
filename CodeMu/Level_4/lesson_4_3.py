#3.1. Дан список. Удалите из него каждый пятый элемент.
def delFiveElement(lst1):
    new_lst = []
    for i in range(len(lst1)):
        if (i+1) % 5 != 0: new_lst.append(lst1[i])
    print(new_lst)


lst1 = [1,4,'g',435,'grd',4,34536,'gvd','grdg','rtdhtsh',7,456,7457]
delFiveElement(lst1)


print()
#3.2. Даны два числа. Получите список общих делителей этих чисел.
def listDel(int1,int2):
    list1 = []
    list2 = []
    o_list = []
    for i in range(1,int1+1):
        if int1 % i == 0: list1.append(i)
    for j in range(1,int2+1):
        if int2 % j == 0: list2.append(j)

    if len(list1) > len(list2):
        big = list1
        small = list2
    else:
        big = list2
        small = list1

    for i in big:
        if i in small: o_list.append(i)
    print(o_list)

int1, int2 = 1234, 123456
listDel(int1,int2)


print()
#3.3. Даны два числа: txt1 = 12345 и txt2 = 45678. Получите кортеж цифр, которые есть и в одном, и в другом числе: (4, 5)
def intHaveNum(txt1,txt2):
    len_txt1 = [item for item in str(txt1)]
    len_txt2 = [item for item in str(txt2)]
    len_all = []
    for i in len_txt1:
        if i in len_txt2: len_all.append(int(i))
    print(tuple(len_all))


txt1 = 12345
txt2 = 45678
intHaveNum(txt1,txt2)


print()
#3.3. Дан список: [ [ [11, 12, 13], [14, 15, 16], [17, 17, 19], ],
# [ [21, 22, 23], [24, 25, 26], [27, 27, 29], ],
# [ [31, 32, 33], [34, 35, 36], [37, 37, 39], ], ]
# Найдите сумму элементов этого списка.
def sumElemList(lst):
    sum = 0
    for i in lst:
        for j in i:
            for l in j:
                sum += l
    print(sum)

lst = [
	[
		[11, 12, 13],
		[14, 15, 16],
		[17, 17, 19],
	],
	[
		[21, 22, 23],
		[24, 25, 26],
		[27, 27, 29],
	],
	[
		[31, 32, 33],
		[34, 35, 36],
		[37, 37, 39],
	],
]
sumElemList(lst)