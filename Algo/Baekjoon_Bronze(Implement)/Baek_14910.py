import sys

num = list(map(int, sys.stdin.readline().split()))

sortNum = sorted(num)

if sortNum == num:
    print("Good")
else:
    print("Bad")