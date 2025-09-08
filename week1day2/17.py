P = float(input("Enter principal amount (P): "))
r = float(input("Enter annual interest rate (in %): ")) / 100
t = float(input("Enter time in years (t): "))

if t=="compound":
    A = P * (1 + r)**(t)
    CI = A - P
    print(f"Compound Interest: {CI:.2f}")
    print(f"Total Amount: {A:.2f}")
else:
    print("interest ",((P*r*t)/100))
    print("total amount ",)