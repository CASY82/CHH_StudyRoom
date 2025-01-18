import sys
import heapq

m, h, t = map(int, sys.stdin.readline().split())
giant = []

for i in range(m):
    giant.append(int(sys.stdin.readline()))

neg_giant = [-x for x in giant]
heapq.heapify(neg_giant)
cnt = 0

for i in range(t):
    max_val = -heapq.heappop(neg_giant)
    if max_val < h:
        print("YES")
        print(cnt)
        exit()

    if max_val == 1:
        heapq.heappush(neg_giant, -max_val)
        break

    tmp = max_val // 2
    cnt += 1
    heapq.heappush(neg_giant, -tmp)

last_heigth = -heapq.heappop(neg_giant)

if last_heigth < h:
    print("YES")
    print(t)
else:
    print("NO")
    print(last_heigth)

# 다른 사람 풀이
# T 이하만큼 반복

# from heapq import heappush, heappop
#
# N, H, T = map(int, input().split())  # 인구수, 센티의 키, 뿅망치 횟수 제한
# heap = []  # 최대힙
# hammer = 0
#
# for _ in range(N):
#     height = int(input())
#     heappush(heap, -height)
#
# while heap:
#     # 망치 다 썼으면 break
#     if hammer == T:
#         break
#
#     # 다음 사람 : 가장 키가 큰 사람
#     cur = -heap[0]
#
#     # 가장 키가 큰 사람이 센티보다 작거나 1이면 break
#     if cur < H or cur == 1:
#         break
#
#     # 뿅망치 효과가 있는 사람이면 뿅망치 떄리고 heappush, 망치 사용횟수 추가
#     n = heappop(heap)
#     heappush(heap, int(n / 2))
#     hammer += 1
#
#
# if -heap[0] < H:
#     print('YES')
#     print(hammer)
# else:
#     print('NO')
#     print(-heap[0])