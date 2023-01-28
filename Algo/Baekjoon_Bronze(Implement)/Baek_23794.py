import sys

n = int(sys.stdin.readline())

for i in range(n+2):
    for j in range(n+2):
        if i == 0 or i == n+1:
            print("@", end="")
        else:
            if j == 0 or j == n+1:
                print("@", end="")
            else:
                print(" ", end="")

    print()