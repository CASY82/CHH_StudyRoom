import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().strip().split())
    str_num = ''

    for i in range(n, m+1):
        str_num += str(i)

    print(str_num.count('0'))