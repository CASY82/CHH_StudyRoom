import sys

t = int(sys.stdin.readline())

first = [5000000, 3000000, 2000000, 500000, 300000, 100000]
second = [5120000, 2560000, 1280000, 640000, 320000]

for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    result = 0

    # 1차 대회
    tmp = 0
    for i in range(1, 7):
        tmp += i

        if tmp - i <= a <= tmp and a != 0:
            result += first[i-1]
            break

    # 2차 대회
    tmp = 0
    for j in range(5):
        tmp += 2 ** j

        if tmp - (2 ** j) <= b <= tmp and b != 0:
            result += second[j]
            break

    print(result)