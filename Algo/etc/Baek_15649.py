import sys
from itertools import permutations

n, m = map(int, sys.stdin.readline().split())

num = [i+1 for i in range(n)]

result = list(map(list, permutations(num, m)))

for i in range(len(result)):
    for j in range(m):
        print(result[i][j], end=' ')
    print()