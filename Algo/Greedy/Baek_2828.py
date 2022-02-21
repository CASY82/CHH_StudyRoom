import sys

n, m = map(int, sys.stdin.readline().split())
apple = []
j = int(sys.stdin.readline())
result = 0
move = [(i+1) for i in range(m)]

for _ in range(j):
    apple.append(int(sys.stdin.readline()))

for i in range(len(apple)):
    if apple[i] > max(move):
        tmp = abs(apple[i] - max(move))
        result += tmp
        for k in range(len(move)):
            move[k] += tmp
    elif apple[i] < min(move):
        tmp = abs(apple[i] - min(move))
        result += tmp
        for k in range(len(move)):
            move[k] -= tmp
    else:
        continue
print(result)

# 간단하게 할수있는걸;;;
# N, M = map(int, input().split())
# J = int(input())
# apples = [int(input()) for _ in range(J)]
#
# start = 1
# end = M
# result = 0
# for apple in apples:
#     to_move = 0
#     if apple < start:
#         to_move = apple - start
#     elif end < apple:
#         to_move = apple - end
#
#     start += to_move
#     end += to_move
#     result += abs(to_move)
#
# print(result)