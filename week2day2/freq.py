m = input("enter the string ")

di={}

for i in m:
    if i not in di:
        di[i]=1
    else:
        di[i]+=1
print(di)