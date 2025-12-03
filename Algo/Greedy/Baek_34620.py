import sys

a, b = map(int, sys.stdin.readline().split())

# b & (b - 1) == 0 이면 2의 거듭제곱
if b & (b - 1):
    print(-1)
else:
    res = []

    while a > 0:
        # a가 b보다 작다는 것은 마지막 연산이 나누기 2였다는 뜻
        if a < b:
            res.append("K")
            a *= 2
        else:
            res.append("G")
            a -= b

    print("".join(reversed(res)))