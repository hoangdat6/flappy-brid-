arr = []
for i in range(10, 201):
    if (i % 7 == 0) and (i % 5 != 0):
        arr.append(str(i))
print (*arr,sep=",")