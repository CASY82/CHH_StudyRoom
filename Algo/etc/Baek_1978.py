n = int(input())
prime = [True, True] + [False] * 1001
cnt = 0
num = list(map(int, input().split()))

#에라토스테네스의 체
for i in range(2, 1000):
    if prime[i]:
        continue

    j = 2
    while i * j <= 1001:
        prime[i * j] = True
        j += 1

for i in num:
    if not prime[i]:
        cnt += 1

print(cnt)