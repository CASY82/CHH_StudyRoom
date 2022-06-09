import sys

id = sys.stdin.readline().strip()

for i in range(3):
    for j in range(3):
        if i == 1 and j == 1:
            print(":{}:".format(id), end="")
        else:
            print(":fan:", end="")

    print()