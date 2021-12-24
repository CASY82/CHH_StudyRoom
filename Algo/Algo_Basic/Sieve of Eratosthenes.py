#소수 판별 알고리즘

import math

n = 1000

array = [True for i in range(n + 1)]

for i in range(2, int(math.sqrt(n)) + 1):
    if array[i] == True:
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1

for i in range(2, n + 1):
    if array[i]:
        print(i, end=' ')

# 1번 방법이 훨씬 시간이 덜들고 빠르다.
# numer = int(input())
#
# print("1번")
# prime1 = [True] * (numer+1)
# cnt = 0
# for i in range(2, int(numer ** 0.5)+1):
#     if prime1[i]:
#         for j in range(i*i, numer+1, i):
#             cnt += 1
#             prime1[j] = False
#
# print(cnt)
# print("2번")
# prime = [True] * (numer+1)
# cnt = 0
#
# for i in range(2, int(numer ** 0.5)+1):
#     if prime[i]:
#         j = 2
#         while i * j <= numer:
#             cnt += 1
#             prime[i * j] = False
#             j += 1
# print(cnt)
# if prime == prime1:
#     print("똑같다")
# else:
#     print("다르다")