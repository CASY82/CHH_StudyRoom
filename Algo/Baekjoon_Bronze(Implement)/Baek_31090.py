import sys

n = int(sys.stdin.readline())

for _ in range(n):
    year = int(sys.stdin.readline())

    if (year + 1) % (year % 100) == 0:
        print("Good")
    else:
        print("Bye")