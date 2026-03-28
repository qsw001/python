import math

def is_valid(a,b,c):
    if(a+b>c and a+c>b and b+c>a):
        return True

def area(a,b,c):
    s = (a+b+c)/2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    return area

def main():
    a,b,c = int(input("请输入三角型的三个边(如(1,2,3))"))
    if(is_valid(a,b,c)):
        print("三角形面积是",area)
    else:
        print("不能构成三角形")

if __name__ == '__main__':
    main()