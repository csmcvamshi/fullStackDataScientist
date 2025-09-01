sen = input("enter the string:")
l=["a","e","i","o","u"]
v=0
c=0
for i in sen:
    if(l.__contains__(i)):
        v=v+1
    else:
        c=c+1
print("number of vowels :",v)
print("number of consonats :",c)