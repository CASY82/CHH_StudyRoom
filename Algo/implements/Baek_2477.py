# import sys
#
# k = int(sys.stdin.readline())
# verti = []
# horizon = []
#
# for _ in range(6):
#     a, b = map(int, sys.stdin.readline().split())
#
#     if a == 1 or a == 2:
#         verti.append(b)
#     else:
#         horizon.append(b)
#
# max_rec = max(verti) * max(horizon)
#
#
# print(max_rec)
# print(verti, horizon)
# verti.remove(max(verti))
# horizon.remove(max(horizon))
# print(verti, horizon)
# min_rec = verti[0] * horizon[1]
#
# print(k * (max_rec - min_rec))


import sys

k = int(sys.stdin.readline())

side = [0 for _ in range(5)]
bat = []

for _ in range(6):
    direction, length = map(int, sys.stdin.readline().split())

    side[direction] += 1
    bat.append([direction, length])

big_bat = []
small_bat = []

for j in range(len(bat)):
    if side[bat[j][0]] == 1:
        big_bat.append(bat[j][1])
        small_bat.append(abs(bat[(j + 1) % 6][1] - bat[(j - 1) % 6][1]))

print((big_bat[0] * big_bat[1] * k) - (small_bat[0] * small_bat[1] * k))


# 솔루션
# 1. 일단 세로 긴변과 가로 긴변 두개를 찾음
# 2. 그 다음 바로 인접한 짧은 변을 제외하고 나머지 두 변을 곱하면 빼야할 사각형의 크기가 나옴
# 3. 큰 사각형 넓이 - 작은 사각형 넓이

# 1
# 3 60
# 1 20
# 4 160
# 2 50
# 3 100
# 1 30
#
# 6200
#
#
#
# 1
# 4 10
# 2 10
# 4 20
# 2 20
# 3 30
# 1 30
#
# 700