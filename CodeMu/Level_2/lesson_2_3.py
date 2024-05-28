#3.1. Даны два слова. Проверьте, что последняя буква первого слова совпадает с первой буквой второго слова.
def startLatterEndLatter(one_str, two_str):
    if one_str[-1:] == two_str[:1]: print(f"Слово '{two_str}' начинается на ту же букву, на которую заканчивается слово '{one_str}'")
    else: print(f"Первая буква в слове '{two_str}' отличается от последней буквы слова '{one_str}'")

str_one,str_two,str_three = 'торт', 'трон', 'корм'
startLatterEndLatter(str_one, str_two)
startLatterEndLatter(str_two, str_three)


print()
#3.2. Дана некоторая строка. Найдите позицию третьего нуля в строке.
def threeZero(str_zero):
    index_three_zero=0
    index = 0
    count = 0
    if '0' in str_zero:
        while len(str_zero) > index and count < 3:
            if str_zero[index] == '0':
                index_three_zero = index
                count += 1
            index += 1
        if count >= 3: print('Индекс третьего нуля:', index_three_zero)
        else:print('Нулей в строке:', count)
    else:print('Нулей в строке нет')

str_zero_one,str_zero_two,str_zero_three = '5bfgh0ggd3g4g00dr4053v','egr0grhbd','gdrg234r'
threeZero(str_zero_one)
threeZero(str_zero_two)
threeZero(str_zero_three)


print()
#3.3. Даны числа, разделенные запятыми: '12,34,56' Найдите сумму этих чисел.
def sum_num_in_str(str_int):
    list = str_int.split(',')
    sum_num_in_list = 0
    for n in list:
        sum_num_in_list += int(n)
    print(sum_num_in_list)

str_int = '12,34,56'
sum_num_in_str(str_int)


print()
#3.4. Дана дата в следующем формате: '2025-12-31'. Преобразуйте эту дату в следующий словарь:{'year':'2025','month':'12','day': '31'}
def strIdDict(str_date):
    list_for_str = str_date.split('-')
    list_data = ['year', 'month', 'day']
    dict_for_list = dict(zip(list_data, list_for_str))
    print(dict_for_list)

    # или
    dict_for_list = {'year':list_for_str[0],'month':list_for_str[1],'day':list_for_str[2]}
    print(dict_for_list)

str_date = '2025-12-31'
strIdDict(str_date)


print()
#3.5. Дан словарь: { 'a': 1, 'b': 2, 'c': 3, 'd': 4, }. Получите сет его значений: {1, 2, 3, 4}
def dictValueInSet(dict_date):
    dict_date_value = dict_date.values()
    print(set(dict_date_value))

dict_date = { 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 4,}
dictValueInSet(dict_date)