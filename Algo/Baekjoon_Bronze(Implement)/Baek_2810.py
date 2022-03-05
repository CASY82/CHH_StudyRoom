import sys

n = int(sys.stdin.readline())
people = list(sys.stdin.readline())
couple = people.count('L')
result = 0

if couple > 2:
    result += people.count('S')
    result += couple - (couple // 2) + 1
else:
    result += people.count('S')
    result += couple

print(result)