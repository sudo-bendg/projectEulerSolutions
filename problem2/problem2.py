## https://projecteuler.net/problem=2

evenFibs = set()

evenFibs.add(2)

f1 = 1
f2 = 2

while f1 + f2 < 4000000:
    new = f1 + f2
    f1 = f2
    f2 = new
    if f2 % 2 == 0:
        evenFibs.add(f2)

print(sum(evenFibs))