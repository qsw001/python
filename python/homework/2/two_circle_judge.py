import turtle
import math

x1,y1,r1 = eval(input("输入第一个圆的中心坐标和半径如(1,2,3)"))
x2,y2,r2 = eval(input("输入第二个圆的中心坐标和半径如(1,2,3)"))

#判断位置关系
d = math.sqrt((x1-x2)**2+(y1-y2)**2)
if r1+r2 < d:
    print("两圆相离")
if r1+r2 == d:
    print("两圆外切")
if r1+r2 > d:
    if abs(r1-r2) == d:
        print("两圆内切")
    if abs(r1-r2) > d:
        print("两圆内含")
    if abs(r1-r2) < d:
        print("两圆相交")
#turtle作图
turtle.speed(0)
turtle.tracer(0)

turtle.penup()
turtle.goto(x1,y1)
turtle.setheading(-90)
turtle.forward(r1)
turtle.setheading(0)
turtle.pendown()
turtle.circle(r1)

turtle.penup()
turtle.goto(x2,y2)
turtle.setheading(-90)
turtle.forward(r2)
turtle.setheading(0)
turtle.pendown()
turtle.circle(r2)

turtle.update()
turtle.done()