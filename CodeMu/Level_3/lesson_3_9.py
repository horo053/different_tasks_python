#9.1. Дан список с числами. Удалите из него числа, имеющие два и более нуля.
def listWithZeroMoreTwo(list_zero):
    new_list = []
    for i in list_zero:
        count = 0
        for j in str(i):
            if j == '0': count += 1
        if count < 2: new_list.append(i)
    print(new_list)

list_zero = [10, 4, 434, 100, 4040, 3, 450, 530001]
listWithZeroMoreTwo(list_zero)


print()
#9.2. Найдите все числа от 1 до 1000, сумма цифр которых равна 13. Результат запишите в сет.
def intSum13(range_num):
    list_new = []
    for i in range(1,range_num+1):
        sum = 0
        for j in str(i):
            sum = sum + int(j)
        if sum == 13: list_new.append(i)
    print(set(list_new))

range_num = 1000
intSum13(range_num)


print()
#9.3. Дан список:[1, 2, 3] Сделайте так, чтобы в нем каждый элемент повторился два раза: [1, 1, 2, 2, 3, 3]
def addDubleElement(list1):
    new_list = []
    for i in list1:
        new_list.append(i)
        new_list.append(i)
    print(new_list)

list1 = [1, 2, 3]
addDubleElement(list1)


print()
#9.4. Даны два списка: lst1 = [1, 2, 3] и lst2 = [4, 5, 6]. Переберите эти списки одним циклом и в
# каждой итерации выводите их элементы следующим образом:
#'1,4'
#'2,5'
#'3,6'
def listInStr(lst1,lst2):
    for proxy_list,login in list(zip(lst1,lst2)):
        str_int = str(proxy_list) + ',' + str(login)
        print(str_int)

lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
listInStr(lst1,lst2)