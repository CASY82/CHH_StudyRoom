import sys

t = int(sys.stdin.readline())

for _ in range(t):
    array_len = int(sys.stdin.readline())
    array = list(map(int, sys.stdin.readline().split()))

    maximum = -9999

    for i in range(array_len):
        if maximum < array[i]:
            maximum = array[i]
        tmp = array[i]
        j = i + 1
        while j < array_len:
            tmp += array[j]
            if maximum < tmp:
                maximum = tmp
            j += 1

    print(maximum)

# 다른 사람 풀이

# import sys
#
# input = lambda: sys.stdin.readline().strip()
#
# T = int(input())
#
# for _ in range(T):
#     N = int(input())
#     ls = [0] + list(map(int, input().split()))
#
#     prefix_sum = [0] * (N+1)
#     for i in range(1, N+1):
#         prefix_sum[i] = prefix_sum[i-1] + ls[i]
#
#     answer = -1_000_001
#     for i in range(1, N + 1):
#         for j in range(i, N + 1):
#             answer = max(answer, prefix_sum[j] - prefix_sum[i-1])
#
#     print(answer)

# 다른 사람 풀이 2

# for t in range(int(input())):
#   n = int(input())
#   a = list(map(int,input().split()))
#   d = [0]*n
#   d[0] = a[0]
#   for i in range(1,n):
#     d[i] = max(d[i-1]+a[i],a[i])
#   print(max(d))