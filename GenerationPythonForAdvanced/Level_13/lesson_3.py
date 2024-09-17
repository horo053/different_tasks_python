# 1. Даны два комплексных числа. Напишите программу, которая вычисляет и выводит их сумму, разность и произведение.
m = input()
n = input()
print(f"({m}) + ({n}) = {complex(m) + complex(n)}")
print(f"({m}) - ({n}) = {complex(m) - complex(n)}")
print(f"({m}) * ({n}) = {complex(m) * complex(n)}")


# 2. Комплексные числа хранятся в списке numbers. Дополните приведенный код так, чтобы он вывел комплексное число с
# наибольшим модулем и сам модуль числа на отдельных строках.
numbers = [3 + 4j, 3 + 1j, -7 + 3j, 4 + 8j, -8 + 10j, -3 + 2j, 3 - 2j, -9 + 9j, -1 - 1j, -1 - 10j, -20 + 15j,
           -21 + 1j, 1j, -3 + 8j, 4 - 6j, 8 + 2j, 2 + 3j]
s = [abs(i) for i in numbers]
print(numbers[s.index(max(s))], max(s), sep='\n')


# 3. Дано натуральное число n и два комплексных числа z1, z2. Напишите программу, которая вычисляет и выводит
# значение выражения: z1**n + z2**n + z--1**(n) + z--2**(n+1)
n = int(input())
z1 = complex(input())
z2 = complex(input())
print(z1**n + z2**n + z1.conjugate()**n + z2.conjugate()**(n+1))