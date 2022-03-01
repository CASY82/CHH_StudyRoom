import sys
from bisect import bisect_left, bisect_right

t = int(sys.stdin.readline())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    aList = list(map(int, sys.stdin.readline().split()))
    bList = list(map(int, sys.stdin.readline().split()))

    cnt = 0
    bList.sort()

    #단순하게 aList값을 고른뒤 bList의 수와 비교를 하는데 이분 탐색 이용
    for num in aList:
        cnt += bisect_right(bList, num-1)

    print(cnt)