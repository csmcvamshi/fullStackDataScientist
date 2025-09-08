n = int(input("Enter the number: "))
prime_list = []

def isPrime(k):
    if k < 2:
        return False
    for i in range(2, int(k**0.5)+1):
        if k % i == 0:
            return False
    return True

for i in range(1, n+1):
    if isPrime(i):
        prime_list.append(i)

print(prime_list)
