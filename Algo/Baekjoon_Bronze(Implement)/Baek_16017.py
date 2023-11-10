import sys

first = int(sys.stdin.readline())
sec = int(sys.stdin.readline())
third = int(sys.stdin.readline())
last = int(sys.stdin.readline())

ignore = False

if first == 8 or first == 9:
    if sec == third:
        if last == 8 or last == 9:
            ignore = True

if ignore:
    print("ignore")
else:
    print("answer")