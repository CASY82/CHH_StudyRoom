# import sys
#
# n = int(sys.stdin.readline())
# res = 0
# max_length = 0
#
# coordinate = []
#
# b_x, b_y = map(int, sys.stdin.readline().split())
# coordinate.append([b_x, b_y])
#
# for case in range(n - 1):
#     x, y = map(int, sys.stdin.readline().split())
#
#     now_length = abs(b_x - x) + abs(b_y - y)
#     if case != n - 2:
#         max_length = max(max_length, now_length)
#     coordinate.append([x, y])
#
#     b_x, b_y = x, y
#
# for i in range(len(coordinate) - 1):
#     if abs(coordinate[i][0] - coordinate[i + 1][0]) + abs(coordinate[i][1] - coordinate[i + 1][1]) == max_length:
#         coordinate.remove(coordinate[i + 1])
#         break
#
# for final in range(len(coordinate) - 1):
#     res += abs(coordinate[final][0] - coordinate[final + 1][0]) + abs(coordinate[final][1] - coordinate[final + 1][1])
#
# print(res)

import sys

# 입력 받기
n = int(sys.stdin.readline())
coordinates = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 총 거리 계산
total_distance = 0
for i in range(n - 1):
    total_distance += abs(coordinates[i][0] - coordinates[i + 1][0]) + abs(coordinates[i][1] - coordinates[i + 1][1])

# 최소 거리 초기화
min_distance = float('inf')

# 각 체크포인트를 건너뛰는 경우 계산
for i in range(1, n - 1):
    # 현재 체크포인트(i)를 건너뛰었을 때의 거리
    distance_if_skipped = total_distance

    # 건너뛰는 체크포인트와 그 앞뒤 체크포인트 간의 거리
    skip_distance = (
        abs(coordinates[i - 1][0] - coordinates[i + 1][0]) +
        abs(coordinates[i - 1][1] - coordinates[i + 1][1])
    )

    # 현재 체크포인트와 그 앞뒤 체크포인트 간의 거리
    original_distance = (
                            abs(coordinates[i - 1][0] - coordinates[i][0]) +
                            abs(coordinates[i - 1][1] - coordinates[i][1])
                        ) + (
                            abs(coordinates[i][0] - coordinates[i + 1][0]) +
                            abs(coordinates[i][1] - coordinates[i + 1][1])
                        )

    # 총 거리에서 원래 거리 빼고 건너뛰었을 때의 거리 더하기
    distance_if_skipped = distance_if_skipped - original_distance + skip_distance

    # 최소 거리 업데이트
    min_distance = min(min_distance, distance_if_skipped)

# 결과 출력
print(min_distance)
