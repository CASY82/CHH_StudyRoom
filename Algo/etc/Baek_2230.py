import sys

n, m = map(int, sys.stdin.readline().split())

num = []

for _ in range(n):
    num.append(int(sys.stdin.readline()))

num.sort()

first = 0
last = 1
#이게 조건에 안맞아서 틀린거였다... 헐 ㅋㅋ
min_val = sys.maxsize

while last < n:
    tmp = num[last] - num[first]
    if tmp >= m and first < last:
        if min_val > tmp:
            min_val = tmp

        first += 1

    else:
        last += 1

print(min_val)

# import sys
#
# n, m = map(int, sys.stdin.readline().split())
#
# num = []
#
# for _ in range(n):
#     num.append(int(sys.stdin.readline()))
#
# num.sort()
#
# first = 0
# last = 1
# min_val = sys.maxsize
#
# while last < n and first < n:
#     tmp = num[last] - num[first]
#     if tmp == m:
#         print(m)
#         exit(0)
#
#     if tmp < m:
#         last += 1
#         continue
#
#     first += 1
#     min_val = min(min_val, tmp)
#
# print(min_val)