#99乘法表

for i in range(10):
    if i == 0:
        print(end="\t")
        continue
    print(i, end="\t")

print("")

for i in range(9):
    print(i+1,end="\t")
    for j in range(9):
        if(j >= i):
            print((i+1)*(j+1),end="\t")
            continue
        print(end="\t")
          
    print("")