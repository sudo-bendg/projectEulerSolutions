from collections import defaultdict

divisors = {1: 1}

def primeFactorization(n):
    factors = defaultdict(int)
    p = 2
    while p * p <= n:
        while n % p == 0:
            factors[p] += 1
            n //= p
        p += 1
    if n > 1:
        factors[n] += 1
    return factors

def countDivisors(n):
    if n in divisors:
        return divisors[n]

    factor_counts = primeFactorization(n)
    result = 1
    for exponent in factor_counts.values():
        result *= (exponent + 1)

    divisors[n] = result
    return result

done = False
k = 1

while not done:
    n = int(0.5 * k * (k + 1))
    if countDivisors(n) > 500:
        print(n)
        done = True
    k += 1