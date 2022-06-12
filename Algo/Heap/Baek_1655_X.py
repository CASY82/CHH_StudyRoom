# import sys
# from collections import deque

#개념은 우선순위 큐를 이용해서 왼쪽 큐와 오른쪽 큐에 넣는건데, 넣을 때의 규칙을 잘 설정하여야 한다.

# n = int(sys.stdin.readline())
# left = deque()
# right = deque()
#
# for i in range(n):
#     num = int(sys.stdin.readline())
#
#     if (i+1) == 1:
#         left.append(num)
#     elif (i+1) == 2:
#         if num < left[0]:
#             left.append(num)
#         else:
#             right.append(num)
#     else:
#         if num < left[0]:
#             left.append(num)
#         elif left[0] <= num <= right[0]:
#             left.appendleft(num)
#         else:
#             right.append(num)
#
#     print(left[0])

import heapq
import sys

n = int(sys.stdin.readline())

left = []
right = []

for _ in range(n):
    num = int(sys.stdin.readline())

    # left와 rigth의 길이가 같다면 left에 넣어주고(-1 곱해서)
    # 다르다면 right
    if len(left) == len(right):
        heapq.heappush(left, num * -1)
    else:
        heapq.heappush(right, num)

    # left, right에 데이터가 있는 상태에서 left의 데이터가 right의 데이터 보다 클 때
    if len(left) >= 1 and len(right) >= 1 and (left[0] * -1) > right[0]:
        # 그냥 heapq이니 0번째 인줄 알았는데, 해당 방법으로 하면 몇몇의 케이스가 통과가 안된다. 최적이 아니라고 판단되는듯
        # 이부분도 heapq로만 해야됨
        left_max = heapq.heappop(left) * -1
        right_max = heapq.heappop(right)

        heapq.heappush(left, right_max * -1)
        heapq.heappush(right, left_max)

    print(left[0] * -1)