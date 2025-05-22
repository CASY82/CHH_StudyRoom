import sys

t = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

for num in nums:
    tmp = []
    for i in range(1, num):
        if num % i == 0:
            tmp.append(i)

    if sum(tmp) == num:
        print("Perfect")
    elif sum(tmp) < num:
        print("Deficient")
    else:
        print("Abundant")