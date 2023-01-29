import sys

n = int(sys.stdin.readline())

for i in range(n * 5):
    for j in range(n * 5):
        if i < n:
            print("@", end="")
        else:
            if j < n:
                print("@", end="")
            else:
                continue

    print()