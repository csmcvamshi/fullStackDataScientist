import time
n=input("enter ")

def getDig(st):
    s=""
    for i in st:
        if(str.isdigit(i)):
            s+=i
    return int(s)

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = f'{mins:02d}:{secs:02d}'
        print(timer, end='\r')
        print(t)
        time.sleep(1)
        t -= 1
countdown(getDig(n))