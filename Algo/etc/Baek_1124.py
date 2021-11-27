a, b = map(int, input().split())

prime = [False, False] + [True] * (b+1)
count = 0

#pypy3로 통과하였으나 여전히 엄청 느리다. 다른 방법을 한번더 강구할 필요가 있다. 그래도 혼자힘으로 해결...
for i in range(2, int(b ** 0.5)+1):
    if prime[i]:
        j = 2
        while j * i <= b:
            prime[i * j] = False
            j += 1

for i in range(a, b+1):
    if prime[i]:
        continue

    tmp = i
    soinsu = []
    j = 2
    while True:
        if tmp == 1:
            break

        if tmp % j == 0:
            tmp //= j
            soinsu.append(j)
        else:
            j += 1

    if prime[len(soinsu)]:
        count += 1

print(count)

#그나마 실행시간이 나은 숏코딩이 아닌 코드 발견!
# def prime_list(n):
#     # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
#     sieve = [True] * n
#
#     # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
#     m = int(n ** 0.5)
#     for i in range(2, m + 1):
#         if sieve[i] == True:  # i가 소수인 경우
#             for j in range(i + i, n, i):  # i이후 i의 배수들을 False 판정
#                 sieve[j] = False
#
#     # 소수 목록 산출
#     return sieve
#
#
# x, y = list(map(int, input().split()))
#
# list = prime_list(y + 1)
# list[1] = False
#
# answer = [0 for _ in range(y + 1)]
# for i in range(1, y + 1):
#     if list[i]:
#         answer[i] = 1
# for i in range(2, y + 1):
#     for j in range(2, y + 1):
#         if i * j > y:
#             break
#         if list[j]:
#             answer[i * j] = answer[i] + 1
# cnt = 0
#
# for i in range(x, y + 1):
#     if list[answer[i]]:
#         cnt += 1
# print(cnt)