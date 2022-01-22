import sys
sys.setrecursionlimit(10 ** 5)

n = int(sys.stdin.readline())
square = [0, 1, 2] + [0] * 1000

def dp(n):
    if n == 1:
        return square[1]

    if n == 2:
        return square[2]

    if square[n] > 0:
        return square[n]

    square[n] = (dp(n-1)+dp(n-2)) % 10007
    return square[n]

print(dp(n))