#3.1. Дана строка. Если в этой строке более одного символа, выведите в консоль предпоследний символ этой строки.
def endSymbol(x):
    if len(x) == 0: print("Слово не передано")
    elif len(x) == 1: print("Передана только одна буква:", x)
    else: print(f"Передано слово '{x}' первая буква '{x[0]}'")

a,b,c = "строка","д",""
endSymbol(a)
endSymbol(b)
endSymbol(c)


print()
#3.2. Даны два целых числа. Проверьте, что первое число без остатка делится на второе.
def withoutTrace(one_z, two_z):
    if one_z == 0 or two_z == 0: print("Одно из чисел равно нулю")
    elif one_z % two_z != 0: print(f"Первое число {one_z} не делится на второе число {two_z}")
    else: print(f"Первое число делится на второе число без остатка: {one_z} % {two_z} = 0")

d,e,f,j = 13,4,2,0
withoutTrace(d,e)
withoutTrace(e,f)
withoutTrace(f,j)


print()
#3.3. Дана некоторая строка: 'abcde'. Получите список ее символов: ['a', 'b', 'c', 'd', 'e']. То есть нужно разбить строку в список
def strInList(sil):
    print(list(sil))

h,i = 'abcde',''
strInList(h)
strInList(i)


print()
#3.4. Дан список:[1, 2, 3, 4, 5, 6]. Получите из него следующий срез: [3, 4, 5]
def srez(list_s):
    print(list_s[2:5])

list_s = [1, 2, 3, 4, 5, 6]
srez(list_s)


print()
#3.5. Дан словарь с датой:
#{
#	'year' : '2025',
#	'month': '12',
#	'day'  : '31',
#}
#Из элементов этого словаря соберите дату в следующем формате: '2025-12-31'
def dictDate(dict_d):
    print(f"{dict_d.get('year')}-{dict_d.get('month')}-{dict_d.get('day')}")

dict_d = {'year': '2025', 'month': '12', 'day': '31'}
dictDate(dict_d)