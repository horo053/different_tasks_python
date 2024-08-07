# 1. На вход программе подаётся строка, состоящая из имени и фамилии человека, разделённых одним пробелом.
# Напишите программу, которая проверяет, что имя и фамилия начинаются с заглавной буквы.
s = input()
print('YES' if s == s.title() else 'NO')


# 2. На вход программе подается строка. Напишите программу, которая меняет регистр символов,
# другими словами замените все строчные символы заглавными и наоборот.
s = input()
print(s.swapcase())


# 3. На вход программе подается строка текста. Напишите программу, которая определяет является ли оттенок текста
# хорошим или нет. Текст имеет хороший оттенок, если содержит подстроку «хорош» во всевозможных регистрах.
# Примечание. Текст содержащий хорош, ХОРОШ, Хорош, хОРОШ и т.д. имеет хороший оттенок.
s = input()
print('YES' if 'хорош' in s.lower() else 'NO')


# 4. На вход программе подается строка. Напишите программу, которая подсчитывает количество буквенных символов в нижнем регистре.
s = input()
s = [i for i in s if i == i.lower() and i not in '1234567890']
print(len(s))
