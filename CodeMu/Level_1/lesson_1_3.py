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
def withoutTrace(oneZ, twoZ):
    if oneZ == 0 or twoZ == 0: print("Одно из чисел равно нулю")
    elif oneZ % twoZ != 0: print(f"Первое число {oneZ} не делится на второе число {twoZ}")
    else: print(f"Первое число делится на второе число без остатка: {oneZ} % {twoZ} = 0")

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
def srez(listS):
    print(listS[2:5])

listS = [1, 2, 3, 4, 5, 6]
srez(listS)


print()
#3.5. Дан словарь с датой:
#{
#	'year' : '2025',
#	'month': '12',
#	'day'  : '31',
#}
#Из элементов этого словаря соберите дату в следующем формате: '2025-12-31'
def dictDate(dictD):
    print(f"{dictD.get('year')}-{dictD.get('month')}-{dictD.get('day')}")

dictD = {'year':'2025', 'month':'12', 'day':'31'}
dictDate(dictD)