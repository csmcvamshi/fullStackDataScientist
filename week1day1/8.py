n = input("enter id ")

i=0
j=len(n)-1

while(i<j):
    if(n[i]!=n[j]):
        print("not a palindrome")
        exit(0)
    i+=1
    j-=1

print("it is a palindrome")