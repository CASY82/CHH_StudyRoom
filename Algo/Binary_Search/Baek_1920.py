# 정렬을 하고 이진탐색을 해라... 라는 뜻
import sys

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
findNum = list(map(int, sys.stdin.readline().split()))

result = []

num.sort()

for i in findNum:
    start = 0
    end = n-1
    check = 0
    while start <= end:
        mid = (start + end) // 2

        if i == num[mid]:
            check = 1
            break

        if i > num[mid]:
            start = mid + 1
        elif i < num[mid]:
            end = mid - 1

    result.append(check)

for i in result:
    print(i)