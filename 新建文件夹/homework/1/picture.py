# 用turtle画出圆，三角形，正方形，最好大小相等
import turtle

#关闭绘画过程，方便调试
turtle.speed(0)
turtle.tracer(0)

#确定初始点位,方便页面内容管理布局
turtle.penup()
turtle.setx(-300)
turtle.pendown()

#圆
turtle.begin_fill()
turtle.color("red")
turtle.circle(100)
turtle.end_fill()
turtle.penup()

#正方形
turtle.forward(150)
turtle.pendown()
turtle.begin_fill()
turtle.color("blue")
for i in range(4):
    turtle.forward(200)
    turtle.left(90)
turtle.end_fill()
turtle.penup()

#三角形
turtle.forward(300)
turtle.pendown()
turtle.begin_fill()
turtle.color("yellow")
for i in range(3):
    turtle.forward(200)
    turtle.left(120)
turtle.end_fill()
turtle.update()
turtle.done()