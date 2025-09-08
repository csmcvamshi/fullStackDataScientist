n = input("Enter the string ")
s = int(input("Enter the shift "))
for i in n :
    k=ord(i)+s
    print(chr(k), end="")
