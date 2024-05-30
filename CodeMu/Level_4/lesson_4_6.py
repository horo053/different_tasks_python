#6.1. Дан список с числами. Оставьте в нем только те числа, которые содержат цифру ноль.
def elementListHaveZero(lst1):
    str_lst1 = [str(item) for item in lst1]
    for i in str_lst1[::-1]:
        if '0' not in i: str_lst1.remove(i)
    int_lst1 = [int(item) for item in str_lst1]
    print(int_lst1)

lst1 = [1,345,46345435,650946,60,540,50604050,43534,23217,8764,309,879354]
elementListHaveZero(lst1)


print()
#6.2. Дана следующая структура: lst = [ { 1: 11, 2: 12, 3: 13, }, { 1: 21, 2: 22, 3: 23, }, { 1: 24, 2: 25, 3: 26, }, ];
# Найдите сумму элементов этой структуры.
def sumElement(lst):
    sum = 0
    for i in lst:
        for j in i.values():
            sum += j
    print(sum)

lst = [
	{
		1: 11,
		2: 12,
		3: 13,
	},
	{
		1: 21,
		2: 22,
		3: 23,
	},
	{
		1: 24,
		2: 25,
		3: 26,
	},
];
sumElement(lst)