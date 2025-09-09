n=input("enter the sentence ")
l=n.split(" ")
s=set()
for i in l:
    s.add(i)
print(s)
print("unique words ",len(s))