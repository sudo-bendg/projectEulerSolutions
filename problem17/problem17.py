## https://projecteuler.net/problem=17

lettersIn = {0: 0,
             1: 3,  # one
             2: 3,  # two
             3: 5,  # three
             4: 4,  # four
             5: 4,  # five
             6: 3,  # six
             7: 5,  # seven
             8: 5,  # eight
             9: 4,  # nine
             10: 3,  # ten
             11: 6,  # eleven
             12: 6,  # twelve
             13: 8,  # thirteen
             14: 8,  # fourteen
             15: 7,  # fifteen
             16: 7,  # sixteen
             17: 9,  # seventeen
             18: 8,  # eighteen
             19: 8,  # nineteen
             20: 6,  # twenty
             30: 6,  # thirty
             40: 5,  # forty
             50: 5,  # fifty
             60: 5,  # sixty
             70: 7,  # seventy
             80: 6,  # eighty
             90: 6,  # ninety
             100: 7,  # hundred
             1000: 8}  # thousand

def numberOfLettersInNumber(num):
    if num <= 20:
        return lettersIn[num]
    elif num < 100:
        tens, ones = divmod(num, 10)
        return lettersIn[tens * 10] + lettersIn[ones]
    elif num < 1000:
        hundreds, remainder = divmod(num, 100)
        if remainder == 0:
            return lettersIn[hundreds] + lettersIn[100]
        else:
            return lettersIn[hundreds] + lettersIn[100] + 3 + numberOfLettersInNumber(remainder)  # 3 for "and"
    elif num == 1000:
        return lettersIn[1] + lettersIn[1000]
    return 0

total = sum(numberOfLettersInNumber(i) for i in range(1, 1001))

print(total)