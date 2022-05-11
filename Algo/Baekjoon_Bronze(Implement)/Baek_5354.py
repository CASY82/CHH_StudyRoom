import sys

t = int(sys.stdin.readline())

for _ in range(t):
    size = int(sys.stdin.readline())

    for i in range(size):
        for j in range(size):
            if i == 0 or i == size-1:
                print("#", end="")
            else:
                if j == 0 or j == size-1:
                    print("#", end="")
                else:
                    print("J", end="")

        print()
    print()