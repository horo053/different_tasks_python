#8.1. С помощью цикла заполните список целыми числами от 1 до 10.
def listAppendForNumLimit(num_limit):
    list_num = []
    for i in range(1,num_limit+1):
        list_num.append(i)
    print(list_num)

num_limit = 10
listAppendForNumLimit(num_limit)


print()
#8.2. Дана строка с буквами. Проверьте, что в этой строке не более двух заглавных букв.
def listAppendForNumLimit(str_upp):
    count = 0
    index = 0
    while len(str_upp) > index:
        if str_upp[index] == str_upp[index].upper(): count += 1
        index += 1
    if count == 0: print(f'В строке "{str_upp}" нет заглавных букв')
    elif count > 2: print(f'В строке "{str_upp}" больше двух заглавных букв')
    else: print(f'В строке "{str_upp}" две заглавные буквы')


str_upp_one,str_upp_two,str_upp_three = 'BdffswDgs','sefesf','sFGesfesBss'
listAppendForNumLimit(str_upp_one)
listAppendForNumLimit(str_upp_two)
listAppendForNumLimit(str_upp_three)


print()
#8.3. Дан список со строками, содержащими целые числа: ['1', '2', '3', '4', '5']
def strListInIntList(str_list):
    int_list = list(int(item) for item in str_list)
    print(int_list)


str_list = ['1', '2', '3', '4', '5']
strListInIntList(str_list)