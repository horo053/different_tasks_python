#10.1. Дана строка с буквами и цифрами. Проверьте, что в этой строке не более трех букв.
def findNum(txt):
    count = 0
    i = 0
    while len(txt) > i:
        if ord(txt[i]) in range(65,91) or ord(txt[i]) in range(97,123) or ord(txt[i]) in range(1040,1103): count += 1
        i+=1
    if count > 3: print(f'В строке "{txt}" количество букв больше трех:', count)
    elif count == 0: print(f'В строке "{txt}" нет букв')
    else: print(f'В строке "{txt}" количество букв равно:', count)

txt1,txt2,txt3 = '435d64eeee6h5gg4m74d56','g9374J84389743h','435345'
findNum(txt1)
findNum(txt2)
findNum(txt3)


print()
#10.2. Дано число. Получите первую четную цифру с конца этого числа.
def chetNumEnd(num):
    chet_num = 1
    while chet_num % 2 != 0:
        if (num % 10) % 2 == 0: chet_num = num % 10
        num //= 10
    print(chet_num)

num = 5123649
chetNumEnd(num)


print()
#10.3. Дана некоторая строка:'abcde abcde abcde'. Замените в ней первый символ каждого слова на '!': '!bcde !bcde !bcde'
def fixOneSymbol(str_one):
    str_replase = str_one.replace('a', '!')
    print(str_replase)

str_one = 'abcde abcde abcde'
fixOneSymbol(str_one)


print()
#10.4. Дан список со строками, содержащими целые числа: ['1', '2', '3', '4', '5'] Найдите сумму элементов этого списка.
def strListInInt(str_list):
    int_list = list(int(item) for item in str_list)
    sum = 0
    for n in int_list:
        sum += n;
    print(sum)

str_list = ['1', '2', '3', '4', '5']
strListInInt(str_list)