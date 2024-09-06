# 1. Дополните приведенный код так, чтобы он вывел сумму минимального и максимального ключа в словаре my_dict.
my_dict = {1.12: 'aa', 67.9: 45, 3.11: 'ccc', 7.9: 'dd', 9.2: 'ee', 7.1: 'ff', 0.12: 'qq', 1.91: 'aa', 10.12: [1, 2, 3], 99.0: {9, 0, 1}}
print(min(my_dict) + max(my_dict))


# 2. Дополните приведенный код, чтобы он вывел имена всех пользователей (в алфавитном порядке), чей номер оканчивается на 8.
users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
         {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
         {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
         {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
         {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
         {'name': 'John', 'phone': '233-421-32', 'email': ''},
         {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
         {'name': 'Alina', 'phone': '+7948-799-2434', 'email': 'ali.ch.b@gmail.com'},
         {'name': 'Robert', 'phone': '420-2011', 'email': ''},
         {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
         {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
         {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
         {'name': 'Roman', 'phone': '+7459-145-8059', 'email': 'roma988@mail.ru'},
         {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
         {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
         {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]
lst = []
for i in users:
    if i['phone'][-1] == '8':
        lst.append(i['name'])
lst.sort()
print(*lst)


# 3. Дополните приведенный код, чтобы он вывел имена всех пользователей (в алфавитном порядке), у которых нет
# информации об электронной почте.
users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
         {'name': 'Helga', 'phone': '555-1618'},
         {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
         {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
         {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
         {'name': 'John', 'phone': '233-421-32', 'email': ''},
         {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
         {'name': 'Alina', 'phone': '+7948-799-2434'},
         {'name': 'Robert', 'phone': '420-2011', 'email': ''},
         {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
         {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
         {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
         {'name': 'Roman', 'phone': '+7459-145-8059'},
         {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
         {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
         {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]
lst = []
for i in users:
    if 'email' not in i.keys() or i['email'] == '':
        lst.append(i['name'])
lst.sort()
print(*lst)


# 4. Напишите программу, которая будет превращать натуральное число в строку, заменяя все цифры в числе на слова
numbers = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'}
n = input()
for i in n:
    for key in numbers:
        if key == i:
            print(numbers[key], end=' ')


# 5. Напишите программу, которая по номеру курса выводит информацию о данном курсе.
course = {'CS101': '3004, Хайнс, 8:00',
          'CS102': '4501, Альварадо, 9:00',
          'CS103': '6755, Рич, 10:00',
          'NT110': '1244, Берк, 11:00',
          'CM241': '1411, Ли, 13:00'}
n = input()
print(f'{n}: {course[n]}')


# 6. На мобильных кнопочных телефонах текстовые сообщения можно отправлять с помощью цифровой клавиатуры.
# Поскольку с каждой клавишей связано несколько букв, для большинства букв требуется несколько нажатий клавиш.
# При однократном нажатии цифры генерируется первый символ, указанный для этой клавиши. Нажатие цифры 2,3,4 или
# 5 раз генерирует второй, третий, четвертый или пятый символ клавиши. Напишите программу, которая отображает нажатия
# клавиш, необходимые для введенного сообщения.
# Примечание: Ваша программа должна обрабатывать как прописные, так и строчные буквы.
keyboard = {".":'1', ",":'11', "?":'111', "!":'1111', ":":'11111',
    "A":'2', "B":'22', "C":'222',
    "D":'3', "E":'33', "F":'333',
    "G":'4', "H":'44', "I":'444',
    "J":'5', "K":'55', "L":'555',
    "M":'6', "N":'66', "O":'666',
    "P":'7', "Q":'77', "R":'777', "S": '7777',
    "T":'8', "U":'88', "V":'888',
    "W":'9', "X":'99', "Y":'999', "Z": '9999',
    " ":'0'}
s = input()
for char in s:
    for key in keyboard:
        if char.upper() == key:
            print(keyboard[key], end='')


# 6. Код Морзе для представления цифр и букв использует тире и точки. Напишите программу для кодирования текстового
# сообщения в соответствии с кодом Морзе.
letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.']
d = dict(zip(letters, morse))
s = input()
for char in s:
    for key in d:
        if char.upper() == key:
            print(d[key], end=' ')