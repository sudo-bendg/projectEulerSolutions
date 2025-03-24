# https://projecteuler.net/problem=37

# Plan: while loop through numbers 11 onwards, looking for primes which are left truncatable and right truncatable
# We can shorten things down by checking if n is prime and if int(str(n)[1:]) / int(str(n)[:-1]) is in the left/right truncatable set
# Done when |leftTruncatable JOIN rightTruncatable| == 11

def isPrime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Initialise these sets with single digit primes, we will remove this later
leftTruncatable = set([2,3,5,7])
rightTruncatable = set([2,3,5,7])

n = 11

done = False
while not done:
    if isPrime(n):
        # is left truncatable
        if int(str(n)[1:]) in leftTruncatable:
            leftTruncatable.add(n)
        # is right truncatable
        if int(str(n)[:-1]) in rightTruncatable:
            rightTruncatable.add(n)
        
        if len(leftTruncatable.intersection(rightTruncatable) - set([2,3,5,7])) == 11:
            done = True
    n += 1

print(sum(leftTruncatable.intersection(rightTruncatable) - set([2,3,5,7])))