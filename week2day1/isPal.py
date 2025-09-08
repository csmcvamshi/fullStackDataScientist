n=input("enter")
k=n.split(" ")
p=""
for i in k:
    p+=i
i=0
j=len(p)-1
while(i<j):
    if(p[i]!=p[j]):
        print("False")
        exit(0)
    i+=1
    j-=1
print("True")