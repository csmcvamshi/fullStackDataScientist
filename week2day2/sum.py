n = int(input("Enter a number: "))

digit_sum = sum(int(d) for d in str(n))
print("Sum of digits:", digit_sum)
