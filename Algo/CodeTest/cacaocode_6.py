# 20210911 6 (정확도 만점, 효율성 박살 0점)

# board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
# skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]

board = [[1,2,3],[4,5,6],[7,8,9]]
skill = [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]

def solution(board, skill):
    answer = 0

    for i in range(len(skill)):
        for j in range(skill[i][1], skill[i][3]+1):
            for k in range(skill[i][2], skill[i][4]+1):
                if skill[i][0] == 1:
                    board[j][k] -= skill[i][5]
                else:
                    board[j][k] += skill[i][5]

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] > 0:
                answer += 1

    return answer

print(solution(board,skill))
