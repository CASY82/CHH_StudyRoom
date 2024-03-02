import sys

n, k = map(int, sys.stdin.readline().split())

arrow = []
history = [0]

for _ in range(n):
    arrow.append(int(sys.stdin.readline()))

point = 0
result = 0

while point != k:
    if arrow[point] not in history:
        history.append(arrow[point])
    else:
        print(-1)
        exit()

    point = arrow[point]
    result += 1

print(result)

# 다른 사람 풀이
# import sys
#
# input = sys.stdin.readline
#
#
# def solution():
#     N, K = map(int, input().split())
#     pairs = [(i, int(input())) for i in range(N)]
#     answer = 0
#
#     idx = 0
#     while True:
#         # K에 도달하지 못하는 경우
#         if answer > N:
#             print(-1)
#             break
#
#         answer += 1
#         target = pairs[idx][1]
#
#         # 0번 인덱스에서 시작하여 K에 도달하는 경우
#         if target == K:
#             print(answer)
#             break
#
#         idx = target
#
#
# solution()