m, n = map(int, input().split())
prime = [True, True] + [False] * (n + 1)

for i in range(2, n + 1):
    if prime[i]:
        continue

    j = 2
    while j * i <= (n+1):
        prime[i * j] = True
        j += 1

for i in range(m, n+1):
    if not prime[i]:
        print(i)

# 실행시간이 아래 방법이 더 빠르다;;;
# prime = []
# primeCheck = [0] * 1000001
#
# M, N = map(int, input().split())
#
# for i in range(2, N+1):
#     if primeCheck[i] == 0:
#         prime.append(i)
#         for j in range(2*i, N+1, i):
#             primeCheck[j] = 1
#
# for i in prime:
#     if i >= M: print(i)