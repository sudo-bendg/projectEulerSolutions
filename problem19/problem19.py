## How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

def leapYear(n):
    return (n % 400 == 0) or (n % 4 == 0 and n % 100 != 0)

months = [31,28,31,30,31,30,31,31,30,31,30,31]

# 1 jan 1901 was a tuesday. This is a 2s day!
dayOfWeek = 2

sundayTheFirsts = 0

for year in range(1901, 2001):
    for month in months:
        # We are looking for the first day of the week to be 0 (mod 7)
        if dayOfWeek % 7 == 0:
            sundayTheFirsts += 1
        dayOfWeek += month

print(sundayTheFirsts)