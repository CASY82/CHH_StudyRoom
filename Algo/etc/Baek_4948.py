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

# 시간 초과
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

#참고용 코드
# import sys
# input=sys.stdin.readline
# def sol():
#     n=123456*2
#     prime=[True]*(n+1)
#     prime[:2]=[False,False]

#     에라토스테네스의 체를 굉장히 짧게 구현한것이 감명 깊었다.
#     for i in range(2,int(n**0.5)+1):
#         if prime[i]:
#             prime[i*2::i]=[False]*(n//i-1)
#     while True:
#         nn=int(input())
#         if nn==0:
#             break
#         나는 한번 더 직접 더하는 시간이 있어서 해당 코드보다 속도는 빨랐으나 메모리가 2배로 사용되었다. 해당 코드는 prime 하나로 해결하였다.
#         print(sum(1 for i in range(nn+1,2*nn+1) if prime[i]))
#
# sol()