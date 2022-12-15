'''
tim so chinh phuong
'''
import math
def square_number(n):
  lis = [0]
  for i in range(1,n+1):
    if i/(math.sqrt(i)) == int(math.sqrt(i)):
      lis.append(i)
  return lis
n=int(input())
print(square_number(n))