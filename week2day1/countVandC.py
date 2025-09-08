n=input("enter ")
l="aeiou"
v=0
c=0
for i in n :
    if (i in l) or (i in l.upper()):
        v+=1
    else:
        c+=1
print("vowels ",v)
print("cosonants ",c)