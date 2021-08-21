#결국 못품... 구현하는 능력이 너무나 떨어진다 해당 소스는 인터넷을 참고한 소스

N, M = map(int, input().split())
board = list()
for i in range(N):
    board.append(input())
repair = list()

for i in range(N-7):
    for j in range(M-7):
        first_W = 0
        first_B = 0
        for k in range(i,i+8):
            for l in range(j,j + 8):
                if (k + l) % 2 == 0:
                    if board[k][l] != 'W':
                        first_W = first_W+1
                    if board[k][l] != 'B':
                        first_B = first_B + 1
                else:
                    if board[k][l] != 'B':
                        first_W = first_W+1
                    if board[k][l] != 'W':
                        first_B = first_B + 1
        repair.append(first_W)
        repair.append(first_B)

print(repair)
print(min(repair))

