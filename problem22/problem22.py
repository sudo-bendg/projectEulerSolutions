names = []

with open("names.txt") as f:
    names = f.read().split('","')

names[0] = names[0].replace('"', '')
names[-1] = names[-1].replace('"', '')

names.sort()

alphabetDict = {chr(i + 65): i + 1 for i in range(26)}

def wordScore(word):
    total = 0
    for char in word:
        total += alphabetDict[char]
    return total

total = 0

for i in range(len(names)):
    total += (i + 1) * wordScore(names[i])

print(total)