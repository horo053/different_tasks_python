#1. Реализуйте функцию hide_card(), которая принимает один аргумент:
# card_number — строка, представляющая собой корректный номер банковской карты из 16 цифр, между которыми могут
# присутствовать символы пробела. Функция должна заменять первые 12 цифр в строке card_number на символ * и возвращать
# полученный результат. Если между цифрами в номере имелись символы пробела, их следует удалить.
def hide_card(card_number):
    card_number = '*' * 12 + card_number.replace(' ', '')[-4:]
    return card_number

card = '1234567890123456'
print(hide_card(card))


#2. Реализуйте функцию same_parity(), которая принимает один аргумент: numbers — список целых чисел.
# Функция должна возвращать новый список, элементами которого являются числа из списка numbers,
# имеющие ту же четность, что и первый элемент этого списка.
def same_parity(numbers):
    numbers = [i for i in numbers if numbers[0]%2 == i%2]
    return numbers

print(same_parity([]))


#3. Будем считать, что PIN-код является корректным, если он удовлетворяет следующим условиям:
# состоит из 4, 5 или 6 символов
# состоит только из цифр (0−9)
# не содержит пробелов
# Реализуйте функцию is_valid(), которая принимает один аргумент: string — произвольная строка
# Функция должна возвращать значение True, если строка string представляет собой корректный PIN-код,
# или False в противном случае.
def is_valid(string):
    return len(string) in [4, 5, 6] and string.isdigit()

print(is_valid('4367'))
print(is_valid('89abc1'))


#4. Реализуйте функцию print_given(), которая принимает произвольное количество позиционных и именованных аргументов
# и выводит все переданные аргументы, указывая тип каждого. Пары аргумент-тип должны выводиться каждая
# на отдельной строке, в следующем формате:
# для позиционных аргументов: <значение аргумента> <тип аргумента>
# для именованных аргументов: <имя переменной> <значение аргумента> <тип аргумента>
def print_given(*args, **kwargs):
    lst_args = []
    lst_kwargs = []
    for i in args:
        lst_args.append(f'{i} {type(i)}')
    for i, j in kwargs.items():
        lst_kwargs.append(f'{i} {j} {type(j)}')
    lst_kwargs.sort()
    lst = lst_args + lst_kwargs
    for i in lst:
        print(i)

    #ИЛИ
    for arg in args:
        print(arg, type(arg))
    for name, value in sorted(kwargs.items()):
        print(name, value, type(value))

print_given(b=2, d=4, c=3, a=1)


#5. Реализуйте функцию convert(), которая принимает один аргумент: string — произвольная строка
# Функция должна возвращать строку string:
# полностью в нижнем регистре, если букв в нижнем регистре в этой строке больше
# полностью в верхнем регистре, если букв в верхнем регистре в этой строке больше
# полностью в нижнем регистре, если количество букв в верхнем и нижнем регистрах в этой строке совпадает
def convert(string=str):
    low = 0
    up = 0
    for i in string:
        if i == i.upper():
            up += 1
        if i == i.lower():
            low += 1
    if low >= up:
        string = string.lower()
    else:
        string = string.upper()
    return string

    #ИЛИ
    a = re.findall(r'[a-z]', s)
    b = re.findall(r'[A-Z]', s)
    return s.lower() if len(a) >= len(b) else s.upper()

print(convert('BEEgeek'))
print(convert('pyTHON'))
print(convert('pi31415!'))


#6. Анаграммы — это слова, которые состоят из одинаковых букв. Например:
# адаптер — петарда
# адресочек — середочка
# азбука — базука
# аистенок — осетинка
# Реализуйте функцию filter_anagrams(), которая принимает два аргумента в следующем порядке:
# word — слово в нижнем регистре
# words — список слов в нижнем регистре
# Функция должна возвращать список, элементами которого являются слова из списка words, которые представляют
# анаграмму слова word. Если список words пуст или не содержит анаграмм, функция должна вернуть пустой список.
def filter_anagrams(word, words):
    words = [i for i in words if ''.join(sorted(word)) == ''.join(sorted(i))]
    return words

word = 'abba'
anagrams = ['aabb', 'abcd', 'bbaa', 'dada']

print(filter_anagrams(word, anagrams))


#7. В различных социальных сетях существуют системы лайков, которые в зависимости от количества людей,
# оценивших запись, показывают соответствующую информацию.
# Реализуйте функцию likes(), которая принимает один аргумент: names — список имён
# Функция должна возвращать строку в соответствии с примерами ниже,
# содержание которой зависит от количества имён в списке names.
def likes(names):
    if len(names) == 1:
        return f'{names[0]} оценил(а) данную запись'
    if len(names) == 2:
        return f'{names[0]} и {names[1]} оценили данную запись'
    if len(names) == 3:
        return f'{names[0]}, {names[1]} и {names[2]} оценили данную запись'
    if len(names) > 3:
        return f'{names[0]}, {names[1]} и {len(names) - 2} других оценили данную запись'
    return 'Никто не оценил данную запись'

print(likes([]))
print(likes(['Тимур']))
print(likes(['Тимур', 'Артур']))
print(likes(['Тимур', 'Артур', 'Руслан']))
print(likes(['Тимур', 'Артур', 'Руслан', 'Анри']))
print(likes(['Тимур', 'Артур', 'Руслан', 'Анри', 'Дима']))
print(likes(['Тимур', 'Артур', 'Руслан', 'Анри', 'Дима', 'Рома', 'Гвидо', 'Марк']))


#8. Реализуйте функцию index_of_nearest(), которая принимает два аргумента в следующем порядке:
# numbers — список целых чисел
# number — целое число
# Функция должна находить в списке numbers ближайшее по значению число к числу number и возвращать его индекс.
# Если список numbers пуст, функция должна вернуть число −1.
def index_of_nearest(numbers, number):
    l = 10000
    res = 0
    if len(numbers) == 0:
        return -1
    else:
        for i, j in enumerate(numbers):
            if abs(j - number) < l:
                l = abs(j - number)
                res = i
        return res


print(index_of_nearest([], 17)) #-1
print(index_of_nearest([7, 13, 3, 5, 18], 0)) #2
print(index_of_nearest([9, 5, 3, 2, 11], 4)) #1
print(index_of_nearest([7, 5, 4, 4, 3], 4)) #2
print(index_of_nearest([6, 100, 101, 2], 4)) #0
print(index_of_nearest([734234423423423, 5343423423546463423, 934234423423423423, -1], 0)) #3
print(index_of_nearest([1, 14, 100, 65, 6], 5)) #4
print(index_of_nearest([10, 164, 100, 265, 16], 8)) #0
print(index_of_nearest([10, 99, 0, -12, 16], -9)) #3
print(index_of_nearest([1, 1, 1, 1, 1], 1)) #0


#9. Реализуйте функцию spell(), которая принимает произвольное количество позиционных аргументов-слов и возвращает
# словарь, ключи которого — первые буквы слов, а значения — максимальные длины слов на эту букву.
def spell(*args):
    args = [i.lower() for i in args]
    d = {key[0]: 0 for key in args}

    for i in args:
        if len(i) > d.get(i[0]):
            d[i[0]] = len(i)

    return d

words = ['россия', 'Австрия', 'австралия', 'РумыниЯ', 'Украина', 'КИТай', 'УЗБЕКИСТАН']
print(spell(*words))
print(spell('Математика', 'История', 'химия', 'биология', 'Информатика'))
words = ['fruit', 'football', 'February', 'forest', 'Family']
print(spell(*words))
print(spell())
words = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa']
print(spell(*words))
words = ['aaaaa', 'aaaaa', 'aaaaa', 'aaaaa', 'aaaaa']
print(spell(*words))
words = ['a']
print(spell(*words))
words = ['a', 'ab', 'abc', 'abcd', 'ба', 'аб', 'абвгдеЁёёЁЁжбБбБввВ', 'ёёё', 'Ёаaа']
print(spell(*words))


#10. Реализуйте функцию choose_plural(), которая принимает два аргумента в следующем порядке:
# amount — натуральное число, количество
# declensions — кортеж из трех вариантов склонения существительного
# Функция должна возвращать строку, полученную путем объединения подходящего существительного из кортежа
# declensions и количества amount, в следующем формате: <количество> <существительное>
def choose_plural(amount, declensions):
    if amount % 10 == 1 and amount % 100 != 11:
        return f'{amount} {declensions[0]}'
    if amount % 10 in (2,3,4) and amount % 100 not in range(11, 21):
        return f'{amount} {declensions[1]}'
    return f'{amount} {declensions[2]}'

print(choose_plural(21, ('пример', 'примера', 'примеров')))
print(choose_plural(92, ('гвоздь', 'гвоздя', 'гвоздей')))
print(choose_plural(8, ('яблоко', 'яблока', 'яблок')))
print(choose_plural(111223, ('копейка', 'копейки', 'копеек')))
print(choose_plural(763434, ('рубль', 'рубля', 'рублей')))
print(choose_plural(512312, ('цент', 'цента', 'центов'))) #
print(choose_plural(59, ('помидор', 'помидора', 'помидоров')))
print(choose_plural(23424157, ('огурец', 'огурца', 'огурцов')))
print(choose_plural(240, ('курица', 'курицы', 'куриц')))
print(choose_plural(49324, ('плюмбус', 'плюмбуса', 'плюмбусов')))
print(choose_plural(505, ('утка', 'утки', 'уток')))
print(choose_plural(666, ('шкаф', 'шкафа', 'шкафов')))
print(choose_plural(11, ('стул', 'стула', 'стульев')))
print(choose_plural(3458438435812, ('доллар', 'доллара', 'долларов')))


#11. Реализуйте функцию get_biggest(), которая принимает один аргумент: numbers — список целых неотрицательных чисел
# Функция должна возвращать наибольшее число, которое можно составить из чисел из списка numbers.
# Если список numbers пуст, функция должна вернуть число −1.
def get_biggest(numbers):
    if numbers:
        max_len_num = len(str(max(numbers)))
        numbers = [str(i) for i in numbers]
        numbers.sort(reverse=True, key=lambda x: x * max_len_num)
        return int(''.join(numbers))
    return -1

print(get_biggest([7, 71, 72]))