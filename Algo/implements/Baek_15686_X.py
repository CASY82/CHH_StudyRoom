import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())

home = []
chick = []

# 거리 비교
def distance(first, second):
    return abs(first[0] - second[0]) + abs(first[1] - second[1])

# 치킨집과 집의 좌표를 모두 구함
for y in range(n):
    x_array = list(map(int, sys.stdin.readline().split()))

    for x in range(len(x_array)):
        if x_array[x] == 1:
            home.append((y + 1, x + 1))
        elif x_array[x] == 2:
            chick.append((y + 1, x + 1))

# 이제 치킨집 m개를 뽑아서 집과 거리를 모두 구한 다음 m개의 치킨집 합이 제일 작은 경우 출력
pick_chick = combinations(chick, m)

result = []

for combination in list(pick_chick):
    tmp_sum = 0
    for house in home:
        tmp = 999
        for chick_house in combination:
            tmp = min(tmp, distance(chick_house, house))

        tmp_sum += tmp

    result.append(tmp_sum)

print(min(result))