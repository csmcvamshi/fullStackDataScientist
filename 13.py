# (Rules: >=90 → A+, 80–89 → A, 70–79 → B, 60–69 → C, <60 → Fail)

n = int(input("Enter the score "))

if(n>=90):
    print("A+")
elif(n>=80):
    print("A")
elif(n>=70):
    print("B")
elif(n>=60):
    print("C")
else:
    print("Fail")