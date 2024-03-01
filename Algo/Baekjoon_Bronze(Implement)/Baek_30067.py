import sys

num = []

for _ in range(10):
    num.append(int(sys.stdin.readline()))

total = sum(num)

for i in range(10):
    if total - num[i] == num[i]:
        print(num[i])
        break