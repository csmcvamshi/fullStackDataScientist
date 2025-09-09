n=int(input("enter the number of sequence "))

def fib(k):
    first=0
    second=1
    if(k==1):
        print(first)
        return 0
    if(k==2):
        print(first,second)
        return 0
    for i in range(1,n+1):
        next=first+second
        print(first)
        first=second
        second=next
fib(n)