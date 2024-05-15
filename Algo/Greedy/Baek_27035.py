import sys

n = int(sys.stdin.readline())
cow_man = []
cow_woman = []
result = 0

for _ in range(n):
    cow_man.append(int(sys.stdin.readline()))

for _ in range(n):
    cow_woman.append(int(sys.stdin.readline()))

cow_man.sort()
cow_woman.sort()

for couple in range(n):
    result += abs(cow_man[couple] - cow_woman[couple])

print(result)