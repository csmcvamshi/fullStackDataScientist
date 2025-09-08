dic={}
n=input("enter the string ")
l = n.split(" ")
for i in l:
    if(i not in dic.keys()):
        dic[i]=1
    else:
        dic[i]+=1
print(dic)