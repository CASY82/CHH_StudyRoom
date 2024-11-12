import sys

t = int(sys.stdin.readline())

# def dolmen(a, b):
#     sum = 0
#
#     for i in range(a + b):
#         for j in range(a + b):
#             for k in range(j):
#                 sum += 1
#
#     return sum

for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())

    # print(dolmen(a, b))
    tmp = (a + b) * ((a + b) * (a + b - 1)) // 2

    print(tmp)