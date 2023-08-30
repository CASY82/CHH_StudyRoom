import sys

n = int(sys.stdin.readline())

fibo = [0 for i in range(46)]

fibo[0] = 1
fibo[1] = 1

for i in range(2, 46):
    fibo[i] = fibo[i-1] + fibo[i-2]

for _ in range(n):
    num = int(sys.stdin.readline())

    print(fibo[num])