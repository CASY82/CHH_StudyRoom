# 틀림
# 동일한 데이터가 있는 사람은 카운트
# 예) [[1, 4], [1, 4], [2, 3], [2, 3], [5, 5]] 본래는 2,3 3,2인데 어쨋든 동일한 순위
# 마지막 동일한 데이터를 기준으로 해당 데이터 보다 큰 데이터들은 카운트 제외
# [[1, 4], [1, 6], [2, 4], [2, 5], [3, 6], [3, 7], [5, 7]]의 경우 동일데이터가 없으므로 0번 인덱스가 기준 그래서 3명

# import sys
#
# t = int(sys.stdin.readline())
#
# for _ in range(t):
#     n = int(sys.stdin.readline())
#     rank = []
#     tmp = []
#     cnt = 0
#
#     for i in range(n):
#         rank.append(list(map(int, sys.stdin.readline().split())))
#
#         # if rank[i][0] > rank[i][1]:
#         #     rank[i][0], rank[i][1] = rank[i][1], rank[i][0]
#
#     rank.sort(key=lambda x: (x[0], x[1]))
#     tmp = rank[0]
#
#     for i in rank:
#         if i[0] <= tmp[0] or i[1] <= tmp[1]:
#             cnt += 1
#         else:
#             break
#
#     print(rank)
#     print(cnt)

    #시간 초과 각
    # tmp = set(map(tuple, rank))
    # tmp = list(map(list, tmp))
    # tmp.sort()
    # print(tmp)

#힌트를 얻음... 정렬은 하나만 하고 두번째만 비교하라는 내용
import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    rank = []
    tmp = []
    cnt = 0

    for i in range(n):
        rank.append(list(map(int, sys.stdin.readline().split())))

    rank.sort(key=lambda x: x[0])
    tmp = rank[0]

    for i in rank:
        if i[1] <= tmp[1]:
            cnt += 1
            tmp[1] = i[1]

    print(cnt)
