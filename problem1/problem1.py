## If we list all the natural numbers below $10$ that are multiples of $3$ or $5$, we get $3, 5, 6$ and $9$. The sum of these multiples is $23$.
## Find the sum of all the multiples of $3$ or $5$ below $1000$

def threesAndFives(n):
    returnSet = set()

    counter = 3

    while counter < n:
        returnSet.add(counter)
        counter += 3
    
    counter = 5

    while counter < n:
        returnSet.add(counter)
        counter += 5
    
    return returnSet

print(sum(threesAndFives(1000)))