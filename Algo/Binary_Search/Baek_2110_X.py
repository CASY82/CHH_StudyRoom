import sys

n, c = map(int, sys.stdin.readline().split())
compareDevice = []

for _ in range(n):
    compareDevice.append(int(sys.stdin.readline()))

compareDevice.sort()

start = 1
end = compareDevice[-1] - compareDevice[0]

while start <= end:
    mid = (start + end) // 2
    cnt = 1
    tmp = compareDevice[0]

    for i in range(1, n):
        #부등호가 둘다 반대였음;;;;;
        if compareDevice[i] >= tmp + mid:
            tmp = compareDevice[i]
            cnt += 1

    #여기도;;; 반대로 했어~~~~~ 아 다 해놓고 왜 답을 못찾니~~~~~
    if cnt >= c:
        #answer가 없어도 틀린다....
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)

#구하는 방법에는 거의 접근했는데 실수가 많았음 그리고 마지막에 result도 없었기에 틀린문제.