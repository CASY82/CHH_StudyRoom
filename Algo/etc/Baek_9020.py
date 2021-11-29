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