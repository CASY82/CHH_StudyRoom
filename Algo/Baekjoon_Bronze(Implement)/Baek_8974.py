import sys

a, b = map(int, sys.stdin.readline().split())
result = 0

easy_arr = []

for num in range(1, 1001):
    cnt = 0

    while cnt < num:
        easy_arr.append(num)
        cnt += 1

print(sum(easy_arr[a-1:b]))