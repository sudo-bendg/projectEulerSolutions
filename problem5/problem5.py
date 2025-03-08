from math import lcm

runningLcm = 1

for n in range(1,11):
    runningLcm = lcm(runningLcm , n)

print(runningLcm)