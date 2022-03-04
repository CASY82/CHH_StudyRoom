import sys

month = int(sys.stdin.readline())
day = int(sys.stdin.readline())

if month > 2:
    print("After")
elif month == 2:
    if day > 18:
        print("After")
    elif day < 18:
        print("Before")
    else:
        print("Special")
else:
    print("Before")