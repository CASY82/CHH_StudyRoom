import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    num = []

    print("Pairs for ", n, ": ", sep="", end="")
    for i in range(1, n):
        if i < n - i:
            num.append([i, n-i])
        else:
            break

    if len(num) > 0:
        for j in range(len(num)):
            if j > 0:
                print(", ", end="")
            print(num[j][0], num[j][1], end="")
    print()