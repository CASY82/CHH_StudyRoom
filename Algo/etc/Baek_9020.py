#혼자힘으로 해내었다...
t = int(input())
prime = [True, True] + [False] * 10000
prime_num = []

for i in range(2, 101):
    if prime[i]:
        continue

    j = 2
    while i * j <= 10001:
        prime[i * j] = True
        j += 1

for i in range(1, 10001):
    if not prime[i]:
        prime_num.append(i)

for _ in range(t):
    n = int(input())

    diff = 10001
    i = 0
    #중간에 >로 해서 틀렸다는게 너무 아쉽다... 당연히 =도 포함해줘야하는데 ㅋㅋ
    while (n // 2) >= prime_num[i]:
        if not prime[(n - prime_num[i])]:
            if diff > abs((n - prime_num[i]) - prime_num[i]):
                diff = abs((n - prime_num[i]) - prime_num[i])
                first = prime_num[i]
                second = n - prime_num[i]

        i += 1

    print(first, second)

#다른사람 참고
# 굉장히 간단한게 나온다는 사실에... 놀랐다 생각해보면 소수를 한번 더 구할 필요가 없었던거 같다.(내 코드에서)
# sosu = [False, False] + [True] * 10000
# for i in range(2, 10001):
#     if sosu[i]:
#         for j in range(2 * i, 10001, i):
#             sosu[j] = False
# t = int(input())
# for i in range(t):
#     n = int(input())
#     for j in range(n // 2, n):
#         if sosu[j] and sosu[n - j]:
#             print(n - j, j)
#             break