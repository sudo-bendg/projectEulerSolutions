## https://projecteuler.net/problem=4

palindromes = set()

def palindrome(n):
    return str(n) == str(n)[::-1]

for i in range(999, 100, -1):
    for j in range(999, 1, -1):
        if palindrome(i * j):
            palindromes.add(i * j)

print(max(palindromes))