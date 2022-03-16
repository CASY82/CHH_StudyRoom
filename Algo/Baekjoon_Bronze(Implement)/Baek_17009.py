import sys
apple = []
banana = []

for i in range(3, 0, -1):
    apple.append(int(sys.stdin.readline()) * i)

for j in range(3, 0, -1):
    banana.append(int(sys.stdin.readline()) * j)

if sum(apple) > sum(banana):
    print("A")
elif sum(apple) < sum(banana):
    print("B")
else:
    print("T")
