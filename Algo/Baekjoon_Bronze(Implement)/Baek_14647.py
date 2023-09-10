import sys

n, m = map(int, sys.stdin.readline().split())

board = []
cnt_table = [[0 for _ in range(m)] for _ in range(n)]
all_cnt = 0

for i in range(n):
    board.append(list(sys.stdin.readline().strip().split()))

for i in range(n):
    for j in range(m):
        cnt_table[i][j] = board[i][j].count("9")
        all_cnt += board[i][j].count("9")

# 각 행의 합을 계산합니다.
row_sums = [sum(row) for row in cnt_table]

# 각 열의 합을 계산합니다.
# 먼저 행과 열을 뒤집어서 열을 행으로 만듭니다.
transposed_matrix = list(map(list, zip(*cnt_table)))
col_sums = [sum(col) for col in transposed_matrix]

print(all_cnt - max(max(row_sums), max(col_sums)))