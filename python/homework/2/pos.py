WIDTH = 10
HEIGHT = 10

x0, y0 = 0, 0

x = int(input("请输入x："))
y = int(input("请输入y："))

if abs(x-x0) <=  WIDTH/2 and abs(y-y0) <= HEIGHT/2:
    print("坐标在矩形内")
else:
    print("坐标在矩形外")
