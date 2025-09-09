n=eval(input("list of students "))

name={}

for i in n:
    if(i not in name ):
        name[i]=1
    else:
        print(i)
        name[i]+=1
