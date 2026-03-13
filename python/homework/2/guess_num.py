#随机生成数字，根据用户输入来判断
import random

random_num = random.randint(10,99)

while True:
    user_num = eval(input("请输入一个两位整数:"))
    if user_num == random_num:
        print("恭喜猜对\n")
        break
    if user_num > random_num:
        print("猜大了\n")
    if user_num < random_num:
        print("猜小了\n")

print("游戏结束")