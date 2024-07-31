# 1. Напишите функцию draw_box(), которая выводит звездный прямоугольник с размерами 14×10
def draw_box():
    for i in range(1,15):
        if i == 1 or i == 14:
            print('*'*10)
        else: print('*' + ' '*8 + '*')

draw_box()


# 2. Напишите функцию draw_triangle(), которая выводит звездный прямоугольный треугольник с катетами, равными 10:
def draw_triangle():
    for i in range(1,11):
        print('*'*i)

draw_triangle()
