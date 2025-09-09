n=eval(input("enter list of marks "))

avg=sum(n)/len(n)

if(avg>=90):
    print("A+")
elif(avg>=80):
    print("A")
elif(avg>=70):
    print("B")
elif(avg>=60):
    print("C")
else:
    print("F")