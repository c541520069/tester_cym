def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print("100以内的质数有：")
primes = [n for n in range(2, 101) if is_prime(n)]
print(primes)
print(f"\n共有 {len(primes)} 个质数")