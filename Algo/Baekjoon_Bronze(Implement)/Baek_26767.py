import sys

n = int(sys.stdin.readline())

for i in range(1, n + 1):
    if i % 7 == 0 and i % 11 == 0:
        print("Wiwat!")
    elif i % 11 == 0:
        print("Super!")
    elif i % 7 == 0:
        print("Hurra!")
    else:
        print(i)