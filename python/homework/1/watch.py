#写一个会动的钟表
import turtle
import time
from datetime import datetime

#实例化类，防止刷新时都消失
draw_time = turtle.Turtle()
draw_watch = turtle.Turtle()
draw_h = turtle.Turtle()
draw_m = turtle.Turtle()
draw_s = turtle.Turtle()
screen = turtle.Screen()

#config
draw_watch.hideturtle()
draw_watch.speed(0)
draw_time.hideturtle()
draw_time.speed(0)
draw_h.hideturtle()
draw_m.hideturtle()
draw_s.hideturtle()
draw_h.speed(0)
draw_m.speed(0)
draw_s.speed(0)
draw_h.pensize(5)
draw_m.pensize(3)
draw_s.pensize(1)
screen.tracer(0)

#画表框
draw_watch.penup()
draw_watch.goto(0,-200)
draw_watch.pendown()
draw_watch.circle(200)

#画12个刻度
draw_watch.penup()
draw_watch.goto(0,0)
for i in range(12):
    draw_watch.forward(190)
    draw_watch.pendown()
    draw_watch.forward(10)
    draw_watch.penup()
    draw_watch.goto(0,0)
    draw_watch.left(30)

#画时钟
draw_time.penup()
draw_time.goto(0,-170)
draw_time.pendown()
while True:
    t = datetime.now()
    curtime = datetime.now().strftime("%H:%M:%S")
    draw_time.write(curtime, align="center", font=("宋体", 20, "normal"))

    #获取时间，获取初始化角度
    hour = t.hour
    minute = t.minute
    second = t.second
    degree_hour = hour*30
    degree_minute = minute*6
    degree_second = second*6

    draw_h.goto(0,0)
    draw_h.pendown()
    draw_h.setheading(90)
    draw_h.right(degree_hour + minute*0.5)
    draw_h.forward(90)
    draw_h.penup()

    draw_m.goto(0,0)
    draw_m.pendown()
    draw_m.setheading(90)
    draw_m.right(degree_minute)
    draw_m.forward(120)
    draw_m.penup()

    draw_s.goto(0,0)
    draw_s.pendown()
    draw_s.setheading(90)
    draw_s.right(degree_second)
    draw_s.forward(150)
    draw_s.penup()

    screen.update()#保持显示流畅，不会出现卡顿
    time.sleep(1)
    draw_time.clear()#clear放在sleep后，防止直接刷新掉
    draw_h.clear()
    draw_m.clear()
    draw_s.clear()

turtle.done()