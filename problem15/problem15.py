## https://projecteuler.net/problem=15

## We are looking for the number of NE lattice paths from (0,0) to (n,n)
## To do this we need to do exactly 2n moves, with exactly n of these being N and n being E
## 2n choose n

from math import comb

n = 20

print(comb(2 * n, n))