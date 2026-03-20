result = 120
i = 0
while result + i*30 <= 1000:
    if i % 10 == 0:
        print("")
    print(result + i*30, end=" ")
    i +=1
