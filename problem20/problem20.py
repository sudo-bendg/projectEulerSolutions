## Find the sum of the digits in the number 100!

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
oneHundredFactorial = factorial(100)
factorialString = str(oneHundredFactorial)
print(sum([int(digit) for digit in factorialString]))