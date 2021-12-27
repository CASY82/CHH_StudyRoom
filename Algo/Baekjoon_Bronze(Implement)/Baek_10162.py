import sys

t = int(sys.stdin.readline())

a = 300
b = 60
c = 10
result = [0] * 3

if t % c != 0:
    print(-1)
else:
    while t > 0:
        if t // a > 0:
            result[0] = t // a
            t %= a

        if t // b > 0:
            result[1] = t // b
            t %= b

        if t // c > 0:
            result[2] = t // c
            t %= c

    print(result[0], result[1], result[2])