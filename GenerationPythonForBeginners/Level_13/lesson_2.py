# 1. Напишите функцию draw_triangle(fill, base), которая принимает два параметра: fill – символ заполнитель;
# base – величина основания равнобедренного треугольника; а затем выводит его.
# Примечание. Гарантируется, что основание треугольника – нечетное число.
def draw_triangle(fill, base):
    for i in range(1,base+1):
        if i <= base//2+1:
            print(fill*i)
        else:
            print(fill*(base-i+1))

fill = input()
base = int(input())

draw_triangle(fill, base)


# 2. Напишите функцию print_fio(name, surname, patronymic), которая принимает три параметра:
# name – имя человека;
# surname – фамилия человека;
# patronymic – отчество человека;
# а затем выводит на печать ФИО человека.
def print_fio(name, surname, patronymic):
    print(surname[0].upper(), end='')
    print(name[0].upper(), end='')
    print(patronymic[0].upper(), end='')

name, surname, patronymic = input(), input(), input()

print_fio(name, surname, patronymic)


# 3. Напишите функцию print_digit_sum(), которая принимает одно натуральное число num и выводит на печать сумму его цифр.
def print_digit_sum(num):
    sum = 0
    while num > 0:
        sum += num%10
        num = num//10
    print(sum)

n = int(input())

print_digit_sum(n)