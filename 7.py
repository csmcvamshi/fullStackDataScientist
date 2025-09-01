import sys as s
a=-s.maxsize-1
for i in range(5):
    n=int(input("Enter the score "))
    a=max(a,n)
print("largest is ",a)