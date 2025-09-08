import math as m
n = int(input("enter the pin: "))
a = n
s=0
len=len(str(n))
while(n>0):
    r=n%10
    s=s+ m.pow(r,len)
    n=n//10
print(f"the entered number is armstrong :{s==a}")