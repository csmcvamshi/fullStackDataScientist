a=int(input("enter num1: "))
b=int(input("enter num2: "))

print("before swapping")
print(f"{a},{b}")
a=a+b
b=a-b
a=a-b
print("after swapping")
print(f"{a},{b}")