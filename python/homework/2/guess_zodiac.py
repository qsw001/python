#猜生肖
year = eval(input("请输入年份"))
zodiac_year = year%12

match zodiac_year:
    case 0:
        print("猴子")
    case 1:
        print("鸡")
    case 2:
        print("狗")
    case 3:
        print("猪")
    case 4:
        print("鼠")   
    case 5:
        print("牛")
    case 6: 
        print("虎")
    case 7:
        print("兔")
    case 8:
        print("龙")
    case 9:
        print("蛇")
    case 10:
        print("马")
    case 11:
        print("羊")

print("游戏结束")