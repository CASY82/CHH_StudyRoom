import sys

n = int(sys.stdin.readline())
buttons = list(map(int, sys.stdin.readline().split()))

res = sum(buttons)

if res >= 1:
    print("Right")
elif res <= -1:
    print("Left")
else:
    print("Stay")