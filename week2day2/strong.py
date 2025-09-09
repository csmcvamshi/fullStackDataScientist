import string as s

flag=False
n=input("enter pass ")
if(len(n)>=8):
    flag=True
punc=s.punctuation
lower=s.ascii_lowercase
dig=s.digits
upp=s.ascii_uppercase

if(any(c in punc for c in n) and any(c in lower for c in n) and any(c in dig for c in n) and any(c in upp for c in n)):
    flag=True
else:
    flag=False

print(flag)
