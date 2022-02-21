import sys

t = int(sys.stdin.readline())

fibo = [0, 1, 1] + [0] * 45

for i in range(3, 48):
    fibo[i] = fibo[i-1] + fibo[i-2]

for _ in range(t):
    n = int(sys.stdin.readline())
    result = []
    tmp = 0

    for i in fibo:
        if n < i:
            tmp = i
            break

    #같은 수를 여러개 쓰는 경우를 생각 안함
    k = fibo.index(tmp)
    while n > 0:
        if n - fibo[k] >= 0:
            n -= fibo[k]
            result.append(fibo[k])
        else:
            k -= 1

    result.reverse()
    print(*result)