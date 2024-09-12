import random
import string

# 1. IP адрес состоит из четырех чисел из диапазона от 0 до 255 (включительно) разделенных точкой.
# Напишите функцию generate_ip(), которая с помощью модуля random  генерирует и возвращает случайный корректный IP адрес.
def generate_ip():
    return f'{random.randrange(256)}.{random.randrange(256)}.{random.randrange(256)}.{random.randrange(256)}'
print(generate_ip())


# 2. Почтовый индекс в Латверии имеет вид: LetterLetterNumber_NumberLetterLetter
# где Letter – заглавная буква английского алфавита, Number – число от 0 до 99 (включительно).
# Напишите функцию generate_index(), которая с помощью модуля random генерирует и возвращает случайный корректный
# почтовый индекс Латверии.
def generate_index():
    return f"{''.join(random.sample(string.ascii_uppercase, 2))}{random.randrange(100)}_{random.randrange(100)}{''.join(random.sample(string.ascii_uppercase, 2))}"

print(generate_index())


# 3. Напишите программу, которая с помощью модуля random перемешивает случайным образом содержимое матрицы (двумерного списка).
matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]
random.shuffle(matrix)
print(matrix)


# 4. Напишите программу, которая с помощью модуля random генерирует 100 случайных номеров лотерейных билетов и
# выводит их каждый на отдельной строке. Обратите внимание, вы должны придерживаться следующих условий:
# номер не может начинаться с нулей;
# номер лотерейного билета должен состоять из 7 цифр;
# все 100 лотерейных билетов должны быть различными.
s = []
for _ in range(100):
    r = random.randint(1000000, 9999999)
    if r not in s:
        s.append(r)
for i in s:
    print(i)


# 5. Анаграмма – это слово образованное путём перестановки букв, составляющих другое слово.
# Например, слова пила и липа или пост и стоп – анаграммы.
# Напишите программу, которая считывает одно слово и выводит с помощью модуля random его случайную анаграмму.
# Примечание: Обратите внимание на то, что метод shuffle() работает со списком, а не со строкой.
word = [i for i in input()]
random.shuffle(word)
print(*word, sep='')


# 6. Для игры в бинго требуется карточка размером 5×5, содержащая различные (уникальные) целые числа от 1 до
# 75 (включительно), при этом центральная клетка является пустой (она заполняется числом 0). Напишите программу,
# которая с помощью модуля random генерирует и выводит случайную карточку для игры в бинго.
num = random.sample(range(1, 76), 25)
num[12] = 0
for i in range(len(num)):
    print(str(num[i]).ljust(3), end = '')
    if i in [4, 9, 14, 19]:
        print()


# 8. Напишите программу, которая с помощью модуля random генерирует n паролей длиной m символов, состоящих из строчных
# и прописных английских букв и цифр, кроме тех, которые легко перепутать между собой:
# «l» (L маленькое);
# «I» (i большое);
# «1» (цифра);
# «o» и «O» (маленькая и большая буквы);
# «0» (цифра).
s = 'abcdefghijkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789'
n = int(input())
m = int(input())
lst = [[random.choice(s) for _ in range(m)] for _ in range(n)]
for i in lst:
    print(*i, sep='')

# ИЛИ
LETTER = ''.join((set(string.ascii_letters) | set(string.digits)) - set('lI1oO0'))

def generate_password(length):
    return ''.join(string.sample(LETTER, length))

def generate_passwords(count, length):
    return [generate_password(length) for _ in range(count)]

n, m = int(input()), int(input())
print(*generate_passwords(n, m), sep='\n')
