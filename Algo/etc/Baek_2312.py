import sys

t = int(sys.stdin.readline())

prime = [False, False] + [True] * 1000000
prime_num = []

for i in range(2, int(1000000 ** 0.5) + 1):
    if prime[i]:
        for j in range(i*i, 1000001, i):
            prime[j] = False

for i in range(len(prime)):
    if prime[i]:
        prime_num.append(i)

for _ in range(t):
    n = int(sys.stdin.readline())
    result = dict()
    i = 0

    while n > 1:
        if n % prime_num[i] == 0:
            if prime_num[i] not in result:
                result[prime_num[i]] = 1
            else:
                result[prime_num[i]] += 1

            n //= prime_num[i]
            i = 0
        else:
            i += 1

    for k, v in result.items():
        print(k, v)