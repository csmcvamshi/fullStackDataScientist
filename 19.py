n = input("enter the pin ")
b = int(input("enter the balance "))
w = int(input("enter the withdrawl amount "))

if(len(n)!=4):
    print("wrong pin")
    exit(0)
new= b-w
if(b<0):
    print("unsuccesful")
else:
    print("successfull , remaining amount ",new)