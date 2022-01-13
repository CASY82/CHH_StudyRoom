import sys

correct = [1,2,3,4,5]
num = list(map(int, sys.stdin.readline().split()))

while num != correct:
    for i in range(len(num)-1):
        j = i + 1
        if num[i] > num[j]:
            num[i], num[j] = num[j], num[i]

            for k in num:
                print(k, end=' ')
            print()