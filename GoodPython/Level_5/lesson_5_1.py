#2. На вход программы подаются два целых положительных числа n и m, записанных через пробел, причем, n < m.
# Необходимо прочитать эти числа и вывести в одну строку через пробел квадраты целых чисел в диапазоне [n; m].
# Программу реализовать при помощи цикла while.
#n, m = map(int, input().split())
#while n <= m:
#    print(n**2, end=' ')
#    n+=1


#3. На вход программы подается вещественное число: стоимость одной книги x рублей.
# Необходимо прочитать это число и вывести на экран в одну строчку через пробел стоимости 2, 3, ... 10-ти
# таких книг с точностью до десятых. Программу реализовать при помощи цикла while.
# price = float(input())
# x = 2
# while x < 11:
#     print(round(x*price, 1), end=" ")
#     x+=1


#4. На вход программы подается целое положительное число n.
# Прочитайте это число, а затем, вычислите и выведите на экран следующую сумму
# с точностью до тысячных (три знака после запятой) Программу реализовать при помощи цикла while.
# n1 = int(input())
# s = 1
# while n1 > 1:
#     s += 1/n1
#     n1-=1
# print(round(s, 3))


#5. Написать программу, в которой пользователь на каждой итерации цикла(while ) должен вводить целое число.
# Цикл должен продолжаться, пока пользователь не введет число 0.
# Необходимо вычислить сумму введенных в цикле чисел и вывести результат (сумму) на экран.
# Программу реализовать при помощи цикла while.
# sum = 0
# n = 1
# while n != 0:
#     n = int(input())
#     sum += n
# print(sum)


#6. На вход программе подается строка (слаг).
# Прочитайте эту строку и замените в ней все подряд идущие дефисы (--, ---, ---- и т.д.) на одинарные (-).
# Результат преобразования строки выведите на экран. Программу реализовать при помощи цикла while.
# str1 = input()
# while "--" in str1:
#     str1 = str1.replace("--", '-')
# print(str1)


#7. На вход программе подается натуральное число (то есть, целое положительное) от трехзначного и более.
# Необходимо прочитать это число и найти произведение всех его цифр. Результат (произведение) вывести на экран.
# Программу реализовать при помощи цикла while.
# int1 = int(input())
# mult = 1
# while int1 > 0:
#     mult *= int1 % 10
#     int1 //= 10
# print(mult)