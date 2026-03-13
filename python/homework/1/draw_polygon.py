import turtle

#config
turtle.speed(0)
turtle.tracer(0)
turtle.hideturtle()

#确定初始位置
turtle.penup()
turtle.goto(-400, 0)
turtle.pendown()

#draw triangle
for i in range(3):
    turtle.forward(100)
    turtle.left(120)

turtle.penup()
turtle.forward(150)
turtle.pendown()

#draw square
for i in range(4):
    turtle.forward(100)
    turtle.left(90)

turtle.penup()
turtle.forward(150)
turtle.pendown()

#draw pentagon
for i in range(5):
    turtle.forward(80)
    turtle.left(360/5)

turtle.penup()
turtle.forward(150)
turtle.pendown()

#draw hesagon
for i in range(6):
    turtle.forward(70)
    turtle.left(360/6)

turtle.penup()
turtle.forward(170)
turtle.pendown()

#draw octagon
for i in range(8):
    turtle.forward(50)
    turtle.left(360/8)

turtle.update()
turtle.done()