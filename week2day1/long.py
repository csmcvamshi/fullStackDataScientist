n = input("enter ")

l=n.split(" ")
leng=l[0]
for i in l:
    if(len(i)>len(leng)):
        leng=i
print(leng)