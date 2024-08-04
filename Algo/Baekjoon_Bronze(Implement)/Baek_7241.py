import sys
import itertools

num = list(map(int, sys.stdin.readline().split()))
check = int(sys.stdin.readline())

permutations = list(itertools.permutations(num))
tmp = []

for n in permutations:
    tmp.append(int("".join(str(x) for x in n)))

tmp.sort()

print(tmp.index(check) + 1)