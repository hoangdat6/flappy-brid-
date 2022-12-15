size = 5
for i in range(size):
    for j in range(i):
        print("",end=" ")
    for j in range(size-i):
        print("*",end=" ")
    print()
    