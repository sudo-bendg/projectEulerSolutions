## https://projecteuler.net/problem=3

def primeFactors(n):
    if n == 1:
        return []
    if n == 2:
        return [2]
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return [i] +  primeFactors(n // i)
    return [n]

print(max(primeFactors(600851475143)))