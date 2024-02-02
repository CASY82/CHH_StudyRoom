import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

result = 0

for i in range(1, n+1):
    for j in range(1, m+1):
        if i + j == 10:
            result += 1

if result == 1:
    print("There is 1 way to get the sum 10.")
else:
    print("There are {0} ways to get the sum 10.".format(result))