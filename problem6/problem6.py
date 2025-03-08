## https://projecteuler.net/problem=6

def sumSquareDifference(n):
    sumOfSquares = sum([n**2 for n in range(1, n+1)])
    squareofSums = sum([n for n in range(1, n+1)]) ** 2

    return squareofSums - sumOfSquares

print(sumSquareDifference(100))