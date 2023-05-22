import sys

arr = []

for _ in range(3):
    arr.append(int(sys.stdin.readline()))

arr.sort()

print(arr[1])