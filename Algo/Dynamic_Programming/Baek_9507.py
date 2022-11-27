import sys

t = int(sys.stdin.readline())
fibo = [1, 1, 2, 4] + [0 for _ in range(64)]

def ggong_fibo(n):
    if n <= 3:
        return fibo[n]
    elif fibo[n] != 0:
        return fibo[n]
    else:
        fibo[n] = ggong_fibo(n - 1) + ggong_fibo(n - 2) + ggong_fibo(n - 3) + ggong_fibo(n - 4)

    return fibo[n]

ggong_fibo(67)

for _ in range(t):
    n = int(sys.stdin.readline())

    print(fibo[n])