import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

def cycle(s):
    length = len(s)
    for i in range(1, n // 2 + 1):
        if length % i == 0:
            tmp = s[:i]
            if tmp * (length // i) == s:
                return "Yes"

    return "No"

print(cycle(s))