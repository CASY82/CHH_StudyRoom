#이진 탐색으로 풀었는데, 나름 생각해보니 투 포인터로 풀어도 된다는 생각이.. 정답 맞추고나서 들었다.
import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
material = list(map(int, sys.stdin.readline().split()))
cnt = 0

material.sort()

for i in range(len(material)):
    compare = material[i+1:]
    start = 0
    end = len(compare)-1

    while start <= end:
        mid = (start + end) // 2

        if material[i] + compare[mid] == m:
            cnt += 1
            break

        if material[i] + compare[mid] < m:
            start = mid + 1
        elif material[i] + compare[mid] > m:
            end = mid - 1

print(cnt)

#투포인터.... 이거 쓸걸... 생각보다 투포인터 활용을 잘 못하고 있는거 같다.
# from sys import stdin
#
# input = stdin.readline
#
# size = int(input().rstrip())
# target = int(input().rstrip())
# numList = sorted(map(int, input().split()))
# start, end, result = 0, size - 1, 0
#
# while start < end:
#     if target > numList[start] + numList[end]:
#         start += 1
#     elif target < numList[start] + numList[end]:
#         end -= 1
#     else:
#         result += 1
#         start += 1
#         end -= 1
#
# print(result)