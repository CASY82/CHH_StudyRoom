import sys
sys.setrecursionlimit(10 ** 5)

n = int(sys.stdin.readline())
num = [0, 1, 3] + [0] * 1000

def dp(n):
    if n == 1:
        return num[1]

    if n == 2:
        return num[2]

    if num[n] > 0:
        return num[n]

    if n % 2 == 0:
        num[n] = (2 * dp(n-1) + 1) % 10007
    else:
        num[n] = (2 * dp(n-1) - 1) % 10007

    return num[n]

print(dp(n))