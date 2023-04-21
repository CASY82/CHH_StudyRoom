import sys

num = int(sys.stdin.readline())

arr = [1, 1, 2, 3] + [0] * 78

for n in range(2, 82):
    arr[n] = arr[n-1] + arr[n-2]

print(arr[num-1] * 2 + arr[num] * 2)