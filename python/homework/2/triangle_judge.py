#三角型判断
import math

while True:
    a,b,c = eval(input("请输入三角型的三个边(如(1,2,3))"))

    if a+b>c and a+c>b and b+c>a:
        s = (a+b+c)/2
        area = math.sqrt(s*(s-a)*(s-b)*(s-c))
        print("该三角形面积是",area)
        break
    else:
        print("该边长构不成三角形，请重新输入")

print("运行结束")