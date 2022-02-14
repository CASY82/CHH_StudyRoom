import sys

n, l = map(int, sys.stdin.readline().split())
loc = list(map(int, sys.stdin.readline().split()))

loc.sort()
i = 0
start = loc[0]
cnt = 0

while i < len(loc)-1:
    i += 1
    if loc[i] - start + 1 > l:
        cnt += 1
        start = loc[i]

print(cnt+1)

# 다른 풀이
# n , l = map(int, input().split())
# loc = list(map(int, input().split()))
# loc.sort()
#
# start = loc[0] # 맨 처음 값을 시작점으로
# cnt = 1 # 필요한 테이프 개수 일단 1개부터 시작
# for i in loc[1:]:
#     if i in range(start, start+l):
#         continue # 시작점 + 테이프 길이 했을 때 i의 값이 이 범위안에 들어오면 기존 테이프를 사용한다는 코드
#     else: # 범위를 넘어가면 새테이프를 사용해야한다는 코드
#         start = i
#         cnt += 1
# print(cnt)