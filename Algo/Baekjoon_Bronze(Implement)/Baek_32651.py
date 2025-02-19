import sys

n = int(sys.stdin.readline())
check = False

if n % 2024 == 0:
    if n <= 100000:
        check = True

if check:
    print("Yes")
else:
    print("No")