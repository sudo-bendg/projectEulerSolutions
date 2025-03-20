# Evaluate the sum of all the amicable numbers under 10000

divSums = dict()
amicableNums = set()

# Find all divisors of a number
def divisorsSum(n):
    divs = set()
    div = 1
    while div * div <= n:
        if n % div == 0:
            # If div is a divisor, so is n / div
            divs.add(div)
            divs.add(n // div)
        div += 1
    return sum(divs) - n

for i in range(2,10001):
    divSum = divisorsSum(i)
    # If the sum of divisors is in our divSums dictionary AND its value is i, we have an am. num.
    if divSum in divSums and divSums[divSum] == i:
        amicableNums.add(i)
        amicableNums.add(divSum)
    # Record the number i and its divisor sum
    divSums[i] = divSum

print(sum(amicableNums))