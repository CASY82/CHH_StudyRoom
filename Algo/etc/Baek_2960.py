import sys

n, k = map(int, sys.stdin.readline().split())
result = 0

prime = [True] * (n+1)
cnt = 0
for i in range(2, n+1):
    if prime[i]:
        cnt += 1
        if cnt == k:
            result = i
            break
        for j in range(i*i, n+1, i):
            if prime[j]:
                cnt += 1
                prime[j] = False

                if cnt == k:
                    result = j
                    break
        if cnt == k:
            break

print(result)