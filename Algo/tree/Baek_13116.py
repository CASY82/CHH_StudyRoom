import sys

t = int(sys.stdin.readline())

for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())

    a_set = []
    b_set = []

    while a > 0:
        a_set.append(a)
        a //= 2

    while b > 0:
        b_set.append(b)
        b //= 2

    max_num = 0

    #같은 것중 제일 큰 수
    for a_num in a_set:
        if a_num in b_set:
            if a_num > max_num:
                max_num = a_num

    print(max_num * 10)