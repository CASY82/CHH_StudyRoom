#중단 너무 어렵다. 아직은 내가 풀 수 있는 레벨은 아닌것 같으며 문제 풀이가 올라오는 경우 참고하는 걸로 하도록 하겠다.

game_board = [[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]]
table = [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]

def solution(game_board, table):
    count = 0

    for i in range(len(game_board)):
        for j in range(len(game_board)):
             if game_board[i][j] == 0:
                game_board[i][j] = 1
                count += 1

    return count



print(solution(game_board, table))