import sys

v = int(sys.stdin.readline())
vote = sys.stdin.readline().strip()

a = 0
b = 0

for i in range(len(vote)):
    if vote[i] == 'A':
        a += 1
    else:
        b += 1

if a == b:
    print("Tie")
elif a > b:
    print("A")
else:
    print("B")