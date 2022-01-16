# 꽃 선택 부분에 있어서 전혀 아이디어가 나오지 않아서... 보고 풀기로 결정(결론 데이터를 포맷팅해서 풀었으면 풀었겠다...)
# import sys
#
# n = int(sys.stdin.readline())
# flower = []
# select = []
# compare = [1, 1, 3, 1]
#
# for _ in range(n):
#     flower.append(list(map(int, sys.stdin.readline().split())))
#
# flower.sort(key= lambda x:(x[0], x[1], x[2], x[3]))
#
# # 선택된 꽃이 3월 1일부터 11월 30일까지 포함
# # 일단 3월 1일 보다 작은일을 가진 애들 중 제일 큰 애를 고른다. --> 항상 고정
# # 선택된 꽃이 지는 날짜보다 작은 애들 중 제일 큰 애를 고른다.
#
# cnt = 0
# for i in range(len(flower)):
#     if compare[2] > flower[i][0]:
#         compare = flower[i]
#         if compare[0] == flower[i][0]:
#             cnt += 1
#         print(compare, cnt)

# import sys
# from collections import deque
#
# n = int(sys.stdin.readline())
# date = []
#
# # 편의를 위해 100을 곱해 날짜 형식으로 바꿈
# for _ in range(n):
#     temp = list(map(int, sys.stdin.readline().split()))
#     date.append([temp[0] * 100 + temp[1], temp[2] * 100 + temp[3]]) # 정말 획기적인 방법이라고 생각된다. 이방법을 생각 못해서 난 4개로 비교 하려다가 실패
#
# # 꽃이 피고 지는 날짜를 오름차순으로 정렬
# date.sort(key=lambda x:(x[0], x[1]))
# date = deque(date)
# # 선택한 꽃의 개수
# cnt = 0
# # 제일 늦게 지는 꽃을 비교
# end = 0
# # 마지막 꽃의 지는 날(여기까진 생각해내었다. 단지 수로 변환하지 않았을뿐)
# target = 301
#
# # 모든 꽃이 없어질 때까지 반복하여 꽃을 비교한다.
# while date:
#     # 마지막 꽃의 지는날이 12월 1일 보다 크거나 같을 때와
#     # 마지막 꽃의 지는날이 제일 빨리 피는 꽃보다 작으면 멈춘다.
#     if target >= 1201 or target < date[0][0]:
#         break
#
#     # 꽃의 개수의 길이만큼 반복하여 구간별로 꽃을 비교한다.
#     for _ in range(len(date)):
#         # 마지막 꽃의 지는 날이 제일 빨리 피는 꽃보다 크거나 같으면 그 꽃의 지는 날을 확인한다.
#         if target >= date[0][0]:
#             # 그 꽃의 지는 날과 마지막으로 꽃의 지는 날을 비교한다.
#             # 그 꽃의 지는 날이 더 크면 더 오래 꽃을 볼 수 있기때문에
#             # 그 꽃의 지는 날을 마지막 꽃의 지는 날로 바꾼다.
#             if end <= date[0][1]:
#                 end = date[0][1]
#
#             # 꽃을 확인 하면 제거한다. 기존 소스에서 큐로 변경
#             #date.remove(date[0])
#             date.popleft()
#
#         # 꽃의 지는 날이 제일 빨리 피는 꽃보다 작으면 멈춰준다.
#         else:
#             break
#
#     # 최종적으로 선택한 꽃의 지는 날을 바꾼다.
#     target = end
#     # 꽃을 선택했으므로 카운트한다.
#     cnt += 1
#
# # 마지막 꽃의 지는 날이 12월 1일보다 작으면 11월 30일에는 피어있는 꽃이 없기때문에 0을 출력
# if target < 1201:
#     print(0)
# else:
#     print(cnt)


import sys
from collections import deque

n = int(sys.stdin.readline())
date = []

for _ in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    date.append([temp[0] * 100 + temp[1], temp[2] * 100 + temp[3]])

date.sort(key=lambda x:(x[0], x[1]))
date = deque(date)
cnt = 0
end = 0
target = 301

while date:
    if target >= 1201 or target < date[0][0]:
        break

    for _ in range(len(date)):
        if target >= date[0][0]:
            if end <= date[0][1]:
                end = date[0][1]

            date.popleft()

        else:
            break

    target = end
    cnt += 1

if target < 1201:
    print(0)
else:
    print(cnt)
