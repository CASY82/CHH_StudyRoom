m = int(input())
n = int(input())
prime = [True, True] + [False] * 10001
result = []

for i in range(2, 10001):
    if prime[i]:
        continue

    j = 2
    while i * j <= 10001:
        prime[i * j] = True
        j += 1

for i in range(m, n+1):
    if not prime[i]:
        result.append(i)

if result:
    print(sum(result))
    print(min(result))
else:
    print(-1)