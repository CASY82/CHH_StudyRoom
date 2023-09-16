import sys

t = int(sys.stdin.readline())

for _ in range(t):
    walk = sys.stdin.readline()
    result = 0

    for i in range(len(walk)):
        if walk[i] == "D":
            break
        elif walk[i] == "U":
            result += 1

    print(result)