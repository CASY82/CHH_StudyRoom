import sys

student = int(sys.stdin.readline())
votes = list(map(int, sys.stdin.readline().split()))

y = 0
n = 0
g = 0

for vote in votes:
    if vote == 1:
        y += 1
    elif vote == -1:
        n += 1
    else:
        g += 1

if g >= student / 2:
    print("INVALID")
else:
    if y > n:
        print("APPROVED")
    else:
        print("REJECTED")