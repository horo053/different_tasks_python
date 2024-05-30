#8.1. Сформируйте с помощью циклов следующий список: [ ['x', 'x', 'x'], ['x', 'x', 'x'], ['x', 'x', 'x'], ]
def listCyrcle(num_range):
    lst1 = []
    lst2 = []
    for i in range(1,num_range+1):
        lst2.append('x')
    for j in range(1,num_range+1):
        lst1.append(lst2)
    print(lst1)

num_range = 3
listCyrcle(num_range)


print()
#8.2. Сформируйте с помощью циклов следующий список:
def listCyrcleTree(num_range_tree):
    lst1 = []
    lst2 = []
    for i in range(1, num_range + 1):
        lst2.append(i)
    for j in range(1, num_range + 3):
        lst1.append(lst2)
    print(lst1)

num_range_tree = 3
listCyrcleTree(num_range_tree)


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