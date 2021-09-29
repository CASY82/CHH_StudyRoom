m = int(input())
n = int(input())
perfect = []

for i in range(1, 101):
    if i * i >= m and i * i <= n:
        perfect.append(i * i)

if not perfect:
    print(-1)
else:
    print(sum(perfect))
    print(min(perfect))