# 1. На вход программе подаётся строка текста, состоящая из слов, разделённых ровно одним пробелом.
# Напишите программу, которая подсчитывает количество слов в ней.
# Примечание 1. Строка текста не содержит пробелов в начале и конце.
s = input()
print(s.count(' ') + 1)


# 2. На вход программе подается строка генетического кода, состоящая из букв А (аденин), Г (гуанин), Ц (цитозин), Т (тимин).
# Напишите программу, которая подсчитывает сколько аденина, гуанина, цитозина и тимина входит в данную строку генетического кода.
# Примечание. Строка не содержит символов, кроме как А, Г, Ц, Т, а, г, ц, т.
s = input().lower()
print('Аденин:', s.count('а'))
print('Гуанин:', s.count('г'))
print('Цитозин:', s.count('ц'))
print('Тимин:', s.count('т'))


# 3. Джим Хоппер с помощью радиоприемника пытается получить сообщение Оди. На приёмник ему поступает n различных
# последовательностей кода Морзе. Декодировав их, он получает последовательности из цифр и букв строчного латинского
# алфавита. При этом только в сообщениях Оди содержится число 11, причём минимум 3 раза.
# Помогите определить Джиму количество сообщений от Оди.
# Примечание. Обратите внимание, что в сообщениях Оди вхождения числа 11 должны быть непересекающимися.
# Другими словами, если мы нашли вхождение числа 11, то следующее вхождение должно начинаться строго после окончания
# предыдущего. Например, в строке '111' содержится одна такая последовательность, в то время как в '1111' их уже две.
n = int(input())
count = 0
for i in range(n):
    s = input()
    if s.count('11') > 2:
        count += 1
print(count)


# 4. На вход программе подается строка текста. Напишите программу, которая подсчитывает количество цифр в данной строке.
n = input()
count = 0
for i in n:
    if i.isdigit():
        count+=1
print(count)


# 5. На вход программе подается строка текста. Напишите программу, которая проверяет, что строка заканчивается подстрокой
n = input()
print('YES' if n.endswith('.ru') or n.endswith('.com') else 'NO')


# 6. На вход программе подаётся строка текста. Напишите программу, которая выводит на экран символ, который появляется наиболее часто.
# Примечание 1. Если таких символов несколько, следует вывести последний по порядку символ.
# Примечание 2. Следует различать заглавные и строчные буквы, а также буквы русского и английского алфавита.
s = input()
c = 0
a = ''
for i in s:
    if s.count(i) >= c:
        c = s.count(i)
        a = i
print(a)


# 7. На вход программе подаётся строка текста. Если в этой строке буква «f» встречается только один раз, выведите её индекс.
# Если она встречается два и более раза, выведите индексы её первого и последнего вхождения на одной строке,
# разделённые символом пробела. Если буква «f» в данной строке не встречается, следует вывести «NO».
n = input()
if n.count('f') == 1:
    print(n.find('f'))
elif n.count('f') == 0:
    print('NO')
else:
    print(n.find('f'), n.rfind('f'))


# 8. На вход программе подаётся строка текста, в которой буква «h» встречается минимум два раза.
# Напишите программу, которая удаляет из этой строки первое и последнее вхождение буквы «h»,
# а также все символы, находящиеся между ними.
n = input()
n1 = n[:n.find('h')]
n2 = n[n.rfind('h')+1:]
print(n1+n2)