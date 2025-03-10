from math import gcd

def a(m, n):
    return m**2 - n**2

def b(m, n):
    return 2 * m * n

def c(m, n):
    return m**2 + n**2

found = False
for m in range(2, 23):  # Limit m based on sqrt(500)
    for n in range(1, m):  # Ensure n < m
        if gcd(m, n) != 1 or (m - n) % 2 == 0:  # Ensure primitive triple conditions
            continue
        sum_abc = 2 * m * (m + n)
        if 1000 % sum_abc == 0:  # Check if 1000 is a multiple of sum_abc
            k = 1000 // sum_abc  # Compute k
            print("m:", m, "n:", n, "k:", k)
            print("a:", k * a(m, n))
            print("b:", k * b(m, n))
            print("c:", k * c(m, n))

            print("product:", k * a(m, n) * k * b(m, n) * k * c(m, n))
        
            found = True
            break
    if found:
        break
