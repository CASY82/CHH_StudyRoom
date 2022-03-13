import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())

    # 0 을 닫기 1을 열기
    prison = [0 for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(i, n+1, i):
            if prison[j] == 0:
                prison[j] = 1
            else:
                prison[j] = 0

    print(prison.count(1))