username = 1
passward = 1
n = 1

def is_prime(N):
    if N <= 1:
        return False
    for i in range(2, int(N**0.5) + 1):
        if N % i == 0:
            return False
    return True

def print_prime_up_to(N):
    primes = [x for x in range(2, N) if is_prime(x)]
    return primes

while n <= 3:
    username = input("Enter your username: ")
    passward = input("Enter your password: ")
    if username == "admin" and passward == "1234":
        N = int(input("Enter number here: "))
        print(print_prime_up_to(N))
        break
    else:
        print("Invalid credentials")
        n = n + 1
        if n > 3:
            print("Account locked")
