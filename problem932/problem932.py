from math import log

numSet = set()

s = 1
odd = 3
counter = 1

while log(s, 10) < 16:
    string = str(s)
    for i in range(1, len(string)):
        a = int(string[:i])
        b = int(string[i:])
        if (a + b) ** 2 == s and string == str(a) + str(b) and a != 0 and b != 0:
            numSet.add(s)
    s += odd
    odd += 2
    if s >= 10 ** counter:
        print(counter, ":", s)
        counter += 1

print(numSet)
print(sum(numSet))