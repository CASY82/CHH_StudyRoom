import sys
import itertools

n, m = map(int, sys.stdin.readline().split())

user_max_love = []
result = 0

for _ in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    max_tmp = []
    for chicken in itertools.combinations(tmp, 3):
        max_tmp.append(max(chicken))

    user_max_love.append(max_tmp)

for i in range(len(user_max_love[0])):
    sum_chicken_love = 0

    for j in range(n):
        sum_chicken_love += user_max_love[j][i]

    if result < sum_chicken_love:
        result = sum_chicken_love

print(result)