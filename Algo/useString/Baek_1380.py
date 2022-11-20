import sys

cnt = 0
while True:
    cnt += 1
    n = int(sys.stdin.readline())

    if n == 0:
        break

    student = []
    check = [0 for _ in range(n)]

    for _ in range(n):
        student.append(sys.stdin.readline().strip())

    for _ in range(2 * n - 1):
        num, card = sys.stdin.readline().strip().split()
        num = int(num)-1

        if check[num] == 1:
            check[num] = 2

        if check[num] == 0:
            check[num] = 1

    print(cnt, student[check.index(1)])