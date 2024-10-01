import sys

n = int(sys.stdin.readline())

dept = []

for _ in range(n):
    times = list(map(int, sys.stdin.readline().split()))

    times = times[1:]

    dept.append(sum(times))

dept.sort()
res = 0

for i in range(n):
    for j in range(i + 1):
       res += dept[j]

print(res)

# 다른 사람 풀이
# import sys
# input = sys.stdin.readline
#
# n = int(input())
# b = []
# for i in range(n):
#     a = list(map(int, input().split()))
#     b.append(sum(a)-a[0])
# b.sort()
# result = 0
# temp = 0
# for num in b:
#     temp += num
#     result += temp
# print(result)