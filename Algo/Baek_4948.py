prime = [True, True] + [False] * (123456 * 2)
prime_count = [0 for i in range(123456 * 2 + 1)]
cnt = 0

for i in range(2, int((123456 * 2) ** 0.5) + 1):
    if prime[i]:
        continue

    j = 2
    while i * j <= (123456 * 2):
        prime[i * j] = True
        j += 1

for i in range(2, (123456 * 2) + 1):
    if not prime[i]:
        cnt += 1

    prime_count[i] = cnt

while True:
    n = int(input())

    if n == 0:
        break

    print(prime_count[n * 2] - prime_count[n])

# while True:
#     n = int(input())
#     prime = [True, True] + [False] * (2 * n)
#     cnt = 0
#     if n == 0:
#         break
#
#     for i in range(2, int((2 * n) ** 0.5) + 1):
#         if prime[i]:
#             continue
#
#         j = 2
#         while i * j <= (2 * n):
#             prime[i * j] = True
#             j += 1
#
#     for i in range(n+1, (2 * n) + 1):
#         if not prime[i]:
#             cnt += 1
#
#     print(cnt)