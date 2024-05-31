#10.1. Дан список: [ [1, 2, 3], [4, 5, 6], [7, 8, 9], ]. Слейте элементы этого списка в один одномерный список: [1, 2, 3, 4, 5, 6, 7, 8, 9]
def listInList(lst):
    str_new = []
    for i in lst:
        for j in i:
            str_new.append(j)
    print(str_new)

lst = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9],
]
listInList(lst)


print()
#10.2. Дан список: [ [2, 1, 4, 3, 5], [3, 5, 2, 4, 1], [4, 3, 1, 5, 2], ]. Отсортируйте элементы в каждом подсписке.
def sortList(lst2):
    for i in lst2:
        i.sort()
    print(lst2)

lst2 = [
	[2, 1, 4, 3, 5],
	[3, 5, 2, 4, 1],
	[4, 3, 1, 5, 2],
]
sortList(lst2)