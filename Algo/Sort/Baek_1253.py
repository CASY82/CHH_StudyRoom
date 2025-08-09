import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

arr.sort()
count = 0

for i in range(N):
    target = arr[i]
    left, right = 0, N - 1

    while left < right:
        if left == i:
            left += 1
            continue
        if right == i:
            right -= 1
            continue

        s = arr[left] + arr[right]

        if s == target:
            count += 1
            break
        elif s < target:
            left += 1
        else:
            right -= 1

print(count)