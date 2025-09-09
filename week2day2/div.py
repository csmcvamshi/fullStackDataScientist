a=int(input("enter a "))
b=int(input("enter b "))

try:
    print(a/b)
except ZeroDivisionError as e:
    print(e)
