board = input().split(".")
result = ''

for i in range(len(board)):
    if i == '':
        result += '.'
    else:
        cnt = board[i].count('X')
        if cnt % 2 == 0:
            AAAA = cnt // 4
            BB = (cnt % 4) // 2
            for _ in range(AAAA):
                result += 'AAAA'
            for _ in range(BB):
                result += 'BB'

            if i != len(board)-1:
                result += '.'
        else:
            result = '-1'
            break

print(result)

# 더 쉬운 풀이;;;
# board = input()
# board = board.replace('XXXX', 'AAAA')
# board = board.replace('XX', 'BB')
# if 'X' in board: print(-1)
# else: print(board)