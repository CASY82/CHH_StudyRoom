import sys

l = 0
t = 0

for _ in range(9):
    vote = sys.stdin.readline().strip()

    if vote == "Lion":
        l += 1
    else:
        t += 1

if l > t:
    print("Lion")
else:
    print("Tiger")