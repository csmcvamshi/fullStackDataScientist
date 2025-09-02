sum=0
for i in range(3):
    print("Enter price for item ",i+1)
    price = int(input(1))
    Quan= int(input("no of items :"))
    sum+= price*Quan
print("sum = ",sum)