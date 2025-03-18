## https://projecteuler.net/problem=14

def collatz_sequence_length(n, cache={1: 1}):
    if n in cache:
        return cache[n]
    if n % 2 == 0:
        length = 1 + collatz_sequence_length(n // 2, cache)
    else:
        length = 1 + collatz_sequence_length(3 * n + 1, cache)
    cache[n] = length
    return length

def longest_collatz_sequence(limit):
    max_length = 0
    starting_number = 0
    for i in range(1, limit):
        length = collatz_sequence_length(i)
        if length > max_length:
            max_length = length
            starting_number = i
    return starting_number

if __name__ == "__main__":
    limit = 1000000
    print(longest_collatz_sequence(limit))