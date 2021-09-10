n, m, l = map(int, input().split())

toss = [0] * (n + 1)
toss[1] = 1
i = 1
count = 0

while max(toss) < m:
    if toss[i] % 2 == 1:
        i += l
        if i > n:
            i = i % n
        toss[i] += 1
    else:
        i -= l
        if i <= 0:
            i = n + i
        toss[i] += 1

    count += 1

print(count)