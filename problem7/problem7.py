## https://projecteuler.net/problem=7

def isPrime(n):
    if n == 2:
        return True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


primes = set()
primes.add(2)

counter = 3

while len(primes) < 10001:
    if isPrime(counter):
        primes.add(counter)
    counter += 2

print(max(primes))