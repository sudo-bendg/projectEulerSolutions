## https://projecteuler.net/problem=10

import time
start_time = time.time()

n = 2000000

prime = [True for i in range(n+1)]
p = 2
while p * p <= n:
    if prime[p]:
        for i in range(p * p, n + 1, p):
            prime[i] = False
    p += 1

primes = [i for i in range(2,n+1) if prime[i]]
print(sum(primes))

print("Process finished --- %s seconds ---" % (time.time() - start_time))