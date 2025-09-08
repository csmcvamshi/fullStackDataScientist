n= input("Enter the sentence ")
v = "aeiou"
c=0
vc=0
l = n.split(" ")
print("sentences ",len(l))

for i in n:
    if i in v or i in v.lower():
        vc+=1
    c+=1
print("chars ",c)
print("vowels ",v)