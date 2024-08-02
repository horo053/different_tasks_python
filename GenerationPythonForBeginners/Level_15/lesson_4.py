# Описание проекта: программа генерирует заданное количество паролей и включает в себя умную настройку на длину пароля,
# а также на то, какие символы требуется в него включить, а какие исключить.
import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'

chars = ''

print('Какое количество паролей для генерации вам нужно?')
kol = int(input())

print('Введите длину пароля')
d = int(input())

print('Включать ли цифры 0123456789?')
c = input()

print('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?')
p = input()

print('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?')
s = input()

print('Включать ли символы !#$%&*+-=?@^_?')
sym = input()


if c == 'да':
    chars += digits
if p == 'да':
    chars += uppercase_letters
if s == 'да':
    chars += lowercase_letters
if sym == 'да':
    chars += punctuation

def generate_password(length, chars):
    passw = ''
    for i in range(length):
        passw += random.choice(chars)
    return passw

for i in range(kol):
    print(generate_password(d, chars))