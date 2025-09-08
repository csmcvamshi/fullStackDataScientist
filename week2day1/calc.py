import math as m

n= input("enter ")
def getDig(st):
    s=""
    for i in st:
        if(str.isdigit(i)):
            s+=i
    return int(s)
if "sqrt" in n:
    print(m.sqrt(getDig(n)))
elif "fac" in n:
    print(m.factorial(getDig(n)))
elif "sin" in n:
    print(m.sin(getDig(n)))
else :
    print(m.cos(getDig(n)))