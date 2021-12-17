import sys

while True:
    num = list(map(int, sys.stdin.readline().split()))

    if not num:
        break

    if len(num) == 1:
        print("Jolly")
        continue

    jolly = []

    for i in range(1, len(num)-1):
        jolly.append(abs(num[i] - num[i+1]))

    jolly.sort()
    check = True
    for i in range(len(jolly)):
        if jolly[i] != (i+1):
            check = False
            break

    if check:
        print("Jolly")
    else:
        print("Not jolly")