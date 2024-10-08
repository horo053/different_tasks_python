# 1. Напишите программу для вывода количества уникальных символов каждого считанного слова без учета регистра.
# На вход программе в первой строке подается число n – общее количество слов. Далее идут n строк с словами.
n = int(input())
lst = [input().lower() for _ in range(n)]
for i in lst:
    print(len(set(i)))


# 2. Напишите программу для вывода общего количества уникальных символов во всех считанных словах без учета регистра.
# На вход программе в первой строке подается число n – общее количество слов. Далее идут n строк с словами.
n = int(input())
s = ''.join([input().lower() for _ in range(n)])
print(len(set(s)))


# 3. Напишите программу для определения общего количества различных слов в строке текста. На вход программе подается строка текста.
# Примечание 1. Словом считается последовательность непробельных символов, идущих подряд, слова разделены одним или большим числом пробелов.
# Примечание 2. Знаками препинания .,;:-?! пренебрегаем.
words = [word.lower().strip('.,;:-?!') for word in input().split()]
print(len(set(words)))


# 4. На вход программе подается строка текста, содержащая числа. Для каждого числа выведите слово YES (в отдельной строке),
# если это число ранее встречалось в последовательности или NO, если не встречалось. На вход программе подается строка
# текста, содержащая числа, разделенные символом пробела.
s = list(map(int, input().split()))
se = set(s)
d = dict()
for i in se:
    d.setdefault(i, 0)
for i in s:
    if d.get(i) > 0:
        print('YES')
    else:
        print('NO')
        d[i] += 1

# ИЛИ
numbers = [int(i) for i in input().split()]
myset = set()
for i in numbers:
    if i in myset:
        print('YES')
    else:
        print('NO')
        myset.add(i)


# 5.