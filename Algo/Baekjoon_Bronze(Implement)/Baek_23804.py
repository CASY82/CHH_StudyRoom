import sys

n = int(sys.stdin.readline())

for i in range(n*5):
    for j in range(n*5):
        if n > i or n * 5 - n <= i:
            print("@", end="")
        else:
            if j < n:
                print("@", end="")
            else:
                continue

    print()