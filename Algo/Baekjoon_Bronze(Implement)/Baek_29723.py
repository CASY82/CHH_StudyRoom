import sys
from itertools import combinations

elements = list(map(int, sys.stdin.readline().split()))
combinations_list = list(combinations(elements, 3))
cnt = 0

for combo in combinations_list:
    if combo[0] + combo[1] > combo[2] and combo[0] + combo[2] > combo[1] and combo[1] + combo[2] > combo[0]:
        cnt += 1

print(cnt)