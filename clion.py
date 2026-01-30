print("i'm clion1")
print("i'm clion2")
print("i'm clion3")

def clion_add(a,b):
    return a+b

c=clion_add(1,2)
print(c)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = [n for n in range(2, 21) if is_prime(n)]
print(primes)
