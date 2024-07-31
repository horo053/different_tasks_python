# 1. Напишите функцию is_valid_triangle(side1, side2, side3), которая принимает в качестве аргументов три натуральных
# числа, и возвращает значение True если существует невырожденный треугольник со сторонами side1,
# side2, side3 и False в противном случае.
def is_valid_triangle(side1, side2, side3):
    if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
        return True
    else:
        return False

a, b, c = int(input()), int(input()), int(input())

print(is_valid_triangle(a, b, c))


# 2. Напишите функцию is_prime(num), которая принимает в качестве аргумента натуральное число и возвращает значение True,
# если число является простым, или False в противном случае.
def is_prime(num):
    count = 0
    for i in range(1,num+1):
        if num%i == 0:
            count += 1
    if count == 2: return True
    else: return False

n = int(input())

print(is_prime(n))


# 3. Напишите функцию get_next_prime(num), которая принимает в качестве аргумента натуральное число num и
# возвращает первое простое число большее числа num.
def is_prime(num):
    if num == 1:
        return False
    for j in range(2, num):
        if num % j == 0:
            return False
    return True
def get_next_prime(num):
    n = num + 1
    while not is_prime(n):
        n += 1
    return n
n = int(input())
print(get_next_prime(n))


# 4. Напишите функцию is_password_good(password), которая принимает в качестве аргумента строковое значение
# пароля password и возвращает значение True, если пароль является надежным и False - в противном случае.
# Пароль является надежным если:
# его длина не менее 8 символов;
# он содержит как минимум одну заглавную букву (верхний регистр);
# он содержит как минимум одну строчную букву (нижний регистр);
# он содержит хотя бы одну цифру.
def is_password_good(password):
    cu = 0
    cl = 0
    cd = 0
    if len(password) >= 8:
        for i in password:
            if i.isdigit():
                cd += 1
            if i.isupper():
                cu += 1
            if i.islower():
                cl += 1
        if cd>0 and cu>0 and cl>0:
            return True
        else:
            return False
    else:
        return False

txt = input()

print(is_password_good(txt))


# 5. Напишите функцию is_one_away(word1, word2), которая принимает в качестве аргументов два слова word1 и word2 и
# возвращает значение True, если слова имеют одинаковую длину и отличаются ровно в одном символе,
# или значение False  в противном случае.
def is_one_away(word1, word2):
    count = 0
    if len(word1) == len(word2):
        for ind, it in enumerate(word1):
            if it == word2[ind]:
                    count += 1
        if count+1 == len(word2):
            return True
        else:
            return False
    else:
        return False

txt1 = input()
txt2 = input()

print(is_one_away(txt1, txt2))


# 6. Напишите функцию is_palindrome(text), которая принимает в качестве аргумента строку text и возвращает значение
# True если указанный текст является палиндромом и False в противном случае.
def is_palindrome(text):
    s = [' ', ',', '.', '!', '?', '-']
    for i in s:
        text = text.replace(i, '')
    text = text.lower()
    return text == text[::-1]

txt = input()

print(is_palindrome(txt))


# 7. BEEGEEK наконец-то открыл свой банк, в котором используются специальные банкоматы с необычным паролем.
# Действительный пароль BEEGEEK банка имеет вид a:b:c, где a, b и c – натуральные числа. Поскольку основатель
# BEEGEEK фанатеет от математики, то он решил:
# число a – должно быть палиндромом;
# число b – должно быть простым;
# число c – должно быть четным.
# Напишите функцию is_valid_password(password), которая принимает в качестве аргумента строковое значение пароля
# password и возвращает значение True, если пароль является действительным паролем BEEGEEK банка и False - в противном случае.
def is_valid_password(password):
    if password.count(':') == 2:
        p = password.split(':')
        count = 0
        c = 0
        if p[0] == p[0][::-1]:
            count += 1
        for i in range(1, int(p[1])+1):
            if int(p[1]) % i == 0:
                c += 1
        if c == 2:
            count += 1
        if int(p[2]) % 2 == 0:
            count += 1
        return count == 3
    return False

psw = input()

print(is_valid_password(psw))
