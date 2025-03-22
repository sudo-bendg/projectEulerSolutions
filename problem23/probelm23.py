## https://projecteuler.net/problem=23

# Find all divisors of a number
def divisorsSum(n):
    divs = set()
    div = 1
    while div * div <= n:
        if n % div == 0:
            divs.add(div)
            if div != n // div:  # Avoid adding the square root twice
                divs.add(n // div)
        div += 1
    return sum(divs) - n

# Find all abundant numbers under 28124
abundantNums = set(n for n in range(2, 28124) if divisorsSum(n) > n)

# Precompute all sums of two abundant numbers
abundantSums = set()
for a in abundantNums:
    for b in abundantNums:
        if a + b < 28124:
            abundantSums.add(a + b)

# Find all numbers that are not a sum of two abundant numbers
nonSums = {n for n in range(1, 28124) if n not in abundantSums}

# Print the sum of all such numbers
print(sum(nonSums))