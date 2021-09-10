#한번에 컷!
from collections import deque

n, m = map(int, input().split())
export = deque(map(int, input().split()))

count = 0

dq = deque(i for i in range(1, n+1))

while export:
    if export[0] == dq[0]:
        dq.popleft()
        export.popleft()
        continue

    if dq.index(export[0]) > len(dq) - dq.index(export[0]):
        #reverse 즉, 뒤쪽에 가까운 경우
        while dq[0] != export[0]:
            tmp = dq.pop()
            dq.appendleft(tmp)
            count += 1
    else:
        #forward 앞쪽에 가까운 경우
        while dq[0] != export[0]:
            tmp = dq.popleft()
            dq.append(tmp)
            count += 1


print(count)

#다른 사람 코드 참고

# import sys
# from collections import deque
# N, M = map(int, input().split())
# count = 0
# array = deque([x for x in range(1, N + 1)])
# case = list(map(int, sys.stdin.readline().split()))
# for c in case:
#     cur = list(array).index(c)
#     if cur <= len(array) // 2:   #array의 절반보다 큰지 작은지 확인
#         for i in range(cur):
#             array.append(array.popleft())
#     else:
#         cur = len(array) - cur
#         for i in range(cur):
#             array.appendleft(array.pop())
#     count += cur
#     array.popleft()
# print(count)