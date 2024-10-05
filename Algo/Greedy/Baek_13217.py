# import sys
# import heapq
#
# n, m, k = map(int, sys.stdin.readline().split())
# honey = []
#
# for _ in range(n):
#     heapq.heappush(honey, -int(sys.stdin.readline()))
#
# res = 0
# cnt = 0
#
# while cnt < k:
#     now_honey = -heapq.heappop(honey)
#     if now_honey > m:
#         res += m
#         heapq.heappush(honey, -(now_honey-m))
#     else:
#         res += now_honey
#
#     cnt += 1
#
# print(res)

# import sys
#
# n, m, k = map(int, sys.stdin.readline().split())
# honey = []
#
# for _ in range(n):
#     honey.append(int(sys.stdin.readline()))
#
# res = 0
# cnt = 0
#
# while cnt < k:
#     honey.sort()
#     now_honey = honey.pop()
#
#     if now_honey > m:
#         res += m
#         honey.append(now_honey - m)
#     else:
#         res += now_honey
#
#     cnt += 1
#
# print(res)

import sys
import heapq

# 입력 받기
n, m, k = map(int, sys.stdin.readline().split())
honey = []

# 벌집의 꿀 양을 음수로 변환하여 최소 힙에 저장
for _ in range(n):
    heapq.heappush(honey, -int(sys.stdin.readline()))

res = 0

# 최대 K번 수집을 수행
while k > 0 and honey:
    # 현재 가장 많은 꿀이 있는 벌집을 추출 (최댓값)
    now_honey = -heapq.heappop(honey)

    # 현재 벌집에서 수집할 수 있는 최대 꿀 양
    if now_honey > m:
        # 수집할 수 있는 최대 횟수를 계산
        max_collects = min(now_honey // m, k)  # 현재 벌집의 꿀에서 M만큼을 수집할 수 있는 횟수와 K 비교
        res += max_collects * m  # 최대 횟수만큼 M 단위로 수집
        k -= max_collects  # 사용한 횟수만큼 K 감소
        remaining_honey = now_honey - max_collects * m  # 남은 꿀 계산

        # 남은 꿀이 아직 있다면 힙에 다시 추가
        if remaining_honey > 0:
            heapq.heappush(honey, -remaining_honey)

    else:
        # 현재 벌집의 꿀 양이 M 이하라면 한 번에 모두 수집
        res += now_honey
        k -= 1  # 한 번 수집했으므로 K 감소

print(res)