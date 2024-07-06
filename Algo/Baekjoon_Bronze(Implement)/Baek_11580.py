import sys

l = int(sys.stdin.readline())
direct = sys.stdin.readline().strip()

di = "E W S N".split(" ")
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

now = (0, 0)
history = set()

history.add(now)

for i in range(len(direct)):
    nx, ny = now

    nx += dx[di.index(direct[i])]
    ny += dy[di.index(direct[i])]

    now = (nx, ny)

    history.add((nx, ny))

print(len(history))

# 다른 사람 풀이
# l = int(input())
#
# commands = input()
# store = set()
# point = [0, 0]
#
# # 초기 위치 추가
# store.add((point[0], point[1]))
#
# for command in commands:
#     if command == 'E':
#         point[0] += 1
#     elif command == 'W':
#         point[0] -= 1
#     elif command == 'S':
#         point[1] -= 1
#     elif command == 'N':
#         point[1] += 1
#
#     store.add((point[0], point[1]))
#
# print(len(store))
