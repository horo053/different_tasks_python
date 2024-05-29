#6.1. Дан список со числами. Удалите из него числа, состоящие более чем из трех цифр.
def threeNum(num_list):
    new_list = []
    for i in num_list:
        if i // 1000 == 0 and i // 10 != 0 and i // 100 != 0: new_list.append(i)
    print(new_list)

num_list = [4,644,23,788,54645,5]
threeNum(num_list)


print()
#6.2. Дана строка. Проверьте, что эта строка состоит только из цифр.
def onlyNum(str_int):
    count = 0
    for i in str_int:
        if i not in ('1','2','3','4','5','6','7','8','9','0'): count += 1
    if count == 0: print(f'Строка "{str_int}" состоит только из цифр')
    else: print(f'В троке "{str_int}" есть не только цифры, но и буквы')

num_str, not_num_list = '45645485685', 'tfh366jghvn'
onlyNum(num_str)
onlyNum(not_num_list)


print()
#6.3. Дано число, например, вот такое: num = 12345; Проверьте, что все цифры этого числа больше нуля.
def notZero(int_l):
    count = 0
    save_int = int_l
    while int_l > 0:
        if int_l % 10 == 0: count += 1
        int_l //= 10
    if count == 0: print(f"В числе {save_int} нет нулей")
    else:print(f"В числе {save_int} есть нули")

int_zero, int_no_zero = 4058, 12345
notZero(int_zero)
notZero(int_no_zero)


print()
#6.4. Даны два списка: lst1 = [1, 2, 3, 4, 5] и lst2 = [1, 2, 3]. Проверьте, что все элементы первого списка есть во втором.
def orderList(lst1,lst2):
    count = 0
    for i in lst1:
        if i in lst2: count += 1
    if count == len(lst1): print("Все элементы первого списка есть во втором")
    else: print("Не все элементы первого списка есть во втором")

lst1 = [1, 2, 3, 4, 5]
lst2 = [1, 2, 3]
orderList(lst1,lst2)