import sys

n, k = map(int, sys.stdin.readline().split())
res = []

def func(n):
    return n % 10

result_k = func(k)
result_2k = func(2 * k)

for i in range(1, n + 1):
    now = func(i)
    if result_k == now or result_2k == now:
        continue

    res.append(i)

print(len(res))
print(*res)