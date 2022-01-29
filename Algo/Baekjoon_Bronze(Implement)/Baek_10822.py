import sys

num = sys.stdin.readline().strip().split(",")
sum = 0

for i in num:
    sum += int(i)

print(sum)