import sys

t = int(sys.stdin.readline())

arr = [0 for i in range(1000000)]

arr[0] = 1
arr[1] = 2
arr[2] = 4

for i in range(3, 1000000):
    arr[i] = (arr[i-1] + arr[i-2] + arr[i-3]) % 1000000009

for _ in range(t):
    num = int(sys.stdin.readline())

    print(arr[num-1])