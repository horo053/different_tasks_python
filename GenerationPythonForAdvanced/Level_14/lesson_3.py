import turtle
# 1. Напишите программу, которая рисует изображение домика по образцу.
turtle.showturtle()

turtle.fillcolor('brown')
turtle.begin_fill()
for i in range(3):
  turtle.left(120)
  turtle.forward(100)
turtle.end_fill()

turtle.penup()
turtle.goto(-15,0)
turtle.pendown()

turtle.fillcolor('lightblue')
turtle.begin_fill()
for i in range(4):
  turtle.right(90)
  turtle.forward(70)
turtle.end_fill()


# 2. Напишите программу, которая рисует изображение светофора по образцу.
turtle.showturtle()

turtle.begin_fill()
for i in range(4):
  turtle.right(90)
  if i%2==0:
    turtle.forward(130)
  else:
    turtle.forward(60)
turtle.end_fill()

x = -30
y = -40

color = ['red', 'yellow', 'green']
for i in range(3):
  turtle.penup()
  turtle.goto(x, y)
  turtle.pendown()

  turtle.fillcolor(color[i])
  turtle.begin_fill()
  turtle.circle(15)
  turtle.end_fill()

  y = y - 40


# 3. Напишите программу, которая рисует оптическую иллюзию по образцу.
turtle.showturtle()

for i in range(3):
  turtle.forward(100)
  turtle.left(120)

turtle.pencolor('white')
turtle.penup()
turtle.goto(0,60)
turtle.pendown()

turtle.begin_fill()
for i in range(3):
  turtle.forward(100)
  turtle.right(120)
  turtle.color('black')
  turtle.dot(30)
  turtle.color('white')
turtle.end_fill()


# 4. Напишите программу, которая рисует изображение радуги по образцу.
turtle.showturtle()

color = ['red', 'orange', 'yellow', 'green1', 'MediumSpringGreen', 'cyan', 'DodgerBlue2', 'blue2', 'BlueViolet', 'DeepPink']
r = 50
y = 0

for i in range(10):
  turtle.fillcolor(color[i])
  turtle.begin_fill()
  turtle.circle(r)
  turtle.end_fill()
  r -= 5
  y += 5
  turtle.penup()
  turtle.goto(0,y)
  turtle.pendown()


# 5. Напишите программу, которая рисует изображение полумесяца по образцу.
turtle.showturtle()

turtle.pencolor('blue')
turtle.fillcolor('blue')
turtle.begin_fill()
for i in range(4):
  turtle.left(90)
  turtle.forward(100)
turtle.end_fill()

turtle.pencolor('orange')
turtle.penup()
turtle.goto(-50, 10)
turtle.pendown()

turtle.fillcolor('orange')
turtle.begin_fill()
turtle.circle(40)
turtle.end_fill()

turtle.pencolor('blue')
turtle.penup()
turtle.goto(-40, 10)
turtle.pendown()

turtle.fillcolor('blue')
turtle.begin_fill()
turtle.circle(40)
turtle.end_fill()


