import random as r
import secrets
import string
n=int(input("enter the length "))
def generate_secure_password(length):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for i in range(length))
    
    return password
print(generate_secure_password(n))