# Coral Perfeito
# import sys
#
# while True:
#     line = sys.stdin.readline().strip()
#     if not line:
#         break
#
#     n = int(line)
#     arr = list(map(int, sys.stdin.readline().split()))
#
#     average = sum(arr) / n
#
#     if average == int(average):
#         tmp = 0
#         for i in range(n):
#             tmp = max(tmp, abs(arr[i] - int(average)))
#
#         print(tmp + 1)
#     else:
#         print(-1)

import sys

while True:
    line = sys.stdin.readline().strip()
    if not line:
        break

    n = int(line)
    arr = list(map(int, sys.stdin.readline().split()))

    average = sum(arr) / n

    if average == int(average):
        tmp = 0
        for i in range(n):
            tmp = max(tmp, abs(arr[i] - int(average)))

        print(tmp + 1)
    else:
        print(-1)