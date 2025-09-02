n = eval(input("enter the list of "))
print("max ",max(n))
print("min ",min(n))
sum=0
for i in n:
    sum+=i
print("avg ",sum/len(n) )