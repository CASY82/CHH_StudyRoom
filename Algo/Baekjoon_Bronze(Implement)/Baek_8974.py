import sys

# 비효율적인것은 알고있으나, 이게 제일 쉬워보였다... ㅋㅋ
a, b = map(int, sys.stdin.readline().split())
result = 0

easy_arr = []

for num in range(1, 1001):
    cnt = 0

    while cnt < num:
        easy_arr.append(num)
        cnt += 1

print(sum(easy_arr[a-1:b]))

# 다른 사람 풀이
# a,b=map(int,input().split())
# c = []
# total = 0
# total2 = 0
# for i in range(1,b+1):
#     for j in range(0,i):
#         c.append(i)
#         total += 1
#     if total > b:
#             break
# for i in range(a-1,b):
#     total2 += c[i]
# print(total2)