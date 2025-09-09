n=int(input("enter the units "))
sum=0
if(n<100):
    print(n*5)
elif(n<200):
    print(500+(n-100)*7)
else:
    print(1200+(n-200)*10)