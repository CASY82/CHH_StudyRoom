costs = [[0,0,0], [0,0,0], [0,0,1]]
xcost = 0
ycost = 0

def solution(costs, xcost, ycost):
    answer = 0
    x = 0
    y = 0
    row = len(costs[0])
    col = len(costs)

    while True:
        if x + 1 >= col and y + 1 >= row:
            break

        answer = costs[y][x]
        right = costs[y][x + 1]
        down = costs[y + 1][x]

        if x + 1 < col:
            if (right - xcost) >= 0:
                if (right - xcost) >= (down - ycost):
                    x += 1
                    answer += (right - xcost)
        elif y + 1 < row:
            if (down - ycost) >= 0:
                if (right - xcost) <= (down - ycost):
                    y += 1
                    answer += (down - ycost)


    return answer

print(solution(costs, xcost, ycost))