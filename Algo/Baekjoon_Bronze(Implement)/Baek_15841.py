import sys
sys.setrecursionlimit(50000000)

f = [0] * 491
f[1] = 1
f[2] = 1

def fibo(n):
    if n < 3:
        return 1
    else:
        if f[n] != 0:
            return f[n]
        else:
            f[n] = fibo(n - 1) + fibo(n - 2)
            return f[n]

fibo(490)

while True:
    num = int(sys.stdin.readline())

    if num == -1:
        break

    print("Hour {0}: {1} cow(s) affected".format(num, f[num]))