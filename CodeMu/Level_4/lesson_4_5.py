#5.1. Выведите в консоль все числа в промежутке от 10 до 1000, у которых предпоследняя цифра четная.
def endNumChet(int_range):
    len_int_range = []
    for i in range(10, int_range+1):
        if ((i % 100) // 10) % 2 == 0: len_int_range.append(i)
    print(len_int_range)

int_range = 1000
endNumChet(int_range)


print()
#5.2. Дана строка: '''text1text2text3text4text5'''
def strInList(str1):
    list_str1 = str1.split()
    print(list_str1)

str1 = '''
	text1
	text2
	text3
	text4
	text5
'''
strInList(str1)


print()
#5.2. Дан следующий словарь: dct = { 1: { 1: { 1: 111, 2: 112, 3: 113, }, 2: { 1: 121, 2: 122, 3: 123, }, }, 2: { 1: { 1: 211, 2: 212, 3: 213, }, 2: { 1: 221, 2: 222, 3: 223, }, }, 3: { 1: { 1: 311, 2: 312, 3: 313, }, 2: { 1: 321, 2: 322, 3: 323, }, }, }
# Найдите сумму элементов этого словаря.
def sumDict(dct):
    sum = 0
    for i in dct.values():
        for j in i.values():
            for l in j.values():
                sum += l
    print(sum)

dct = {
	1: {
		1: {
			1: 111,
			2: 112,
			3: 113,
		},
		2: {
			1: 121,
			2: 122,
			3: 123,
		},
	},
	2: {
		1: {
			1: 211,
			2: 212,
			3: 213,
		},
		2: {
			1: 221,
			2: 222,
			3: 223,
		},
	},
	3: {
		1: {
			1: 311,
			2: 312,
			3: 313,
		},
		2: {
			1: 321,
			2: 322,
			3: 323,
		},
	},
}
sumDict(dct)