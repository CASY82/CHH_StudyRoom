#핵심 알고리즘을 몰라서 결국 인터넷 서치 후 문제 해결
n, m = map(int, input().split())

castle = [list(map(str, input())) for _ in range(n)]
col = [0 for i in range(n)]
row = [0 for i in range(m)]


for i in range(n):
    for j in range(m):
        if castle[i][j] == 'X':
            col[i] += 1
            row[j] += 1

#핵심은 행 또는 열 중 인원이 부족한 (즉, 0값이 많은) 데이터를 출력하면 된다.
if col.count(0) > row.count(0):
    print(col.count(0))
else:
    print(row.count(0))


#좀 더 파이썬 다운 코드를 발견하여 첨부
#
# n,m = map(int,input().split())
# castle=[]
#
# for _ in range(n):
#     castle.append(input())
#
# row = []
# col = []
#
# for i in range(n):
#     row.append("X" not in castle[i])
#
# for j in range(m):
#     col.append("X" not in [castle[i][j] for i in range(n)])
#
# print(max(sum(row),sum(col)))