#Greatest Common Divisor

n1 = int(input("输入第一个数："))
n2 = int(input("输入第2个数："))

gcd = 2

while gcd <= n1 and gcd <= n2:
    if n1 % gcd == 0 and n2 % gcd == 0:
        break
    gcd += 1

print("最大公约数为", gcd)