import turtle

# 1. Напишите программу, которая рисует пунктирную линию
turtle.showturtle()
for i in range(5):
    turtle.dot(50)
    turtle.penup()
    turtle.forward(75)


# 2. Напишите программу, которая рисует прямоугольник с точкой в каждом углу
n = 200
m = 100
turtle.showturtle()
for i in range(4):
    turtle.dot(10)
    turtle.forward(n if i%2 == 0 else m)
    turtle.left(90)


# 3. Напишите программу для рисования паутины в соответствии с примером. Программа должна считывать количество
# лучей паутины, число n. Примечание: Угол заданный каждой парой лучей составляет 360/n градусов.
n = int(input())
t = 360 / n

turtle.showturtle()
turtle.shape('triangle')

for i in range(n):
    turtle.forward(100)
    turtle.stamp()
    turtle.backward(100)
    turtle.left(t)

turtle.shape('circle')


# 4. Напишите программу, которая рисует черепашек в соответствии с образцом.
turtle.showturtle()
turtle.shape('turtle')

for i in range(10):
    turtle.penup()
    turtle.forward(50)
    turtle.stamp()
    turtle.penup()
    turtle.backward(50)
    turtle.left(36)

turtle.stamp()


# 5. Напишите программу, которая рисует циферблат часов в соответствии с образцом.
turtle.showturtle()
turtle.shape('turtle')
turtle.pensize(3)

for i in range(12):
    turtle.penup()
    turtle.forward(90)
    turtle.pendown()
    turtle.forward(15)
    turtle.penup()
    turtle.forward(10)
    turtle.stamp()
    turtle.penup()
    turtle.backward(115)
    turtle.left(30)

turtle.stamp()


# 6. Напишите программу, которая рисует черепашью спираль в соответствии с образцом.
turtle.showturtle()
turtle.penup()
turtle.Screen().bgcolor('lightgreen')
turtle.shape('turtle')

n = 38

for i in range(n):
  turtle.forward(i*2)
  turtle.right(22)
  turtle.stamp()

