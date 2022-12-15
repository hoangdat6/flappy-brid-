dk=False


while dk == False:
     Number = int(input())

     Sum = 0
     Times = 0

     Temp = Number
     while Temp > 0:
         Times = Times + 1
         Temp = Temp // 10

     Temp = Number
     while Temp > 0:
        Reminder = Temp % 10
        Sum = Sum + (Reminder ** Times)
        Temp //= 10

     if Number == Sum:
        print("%d is an Armstrong number" %Number)
        dk=True
     
              