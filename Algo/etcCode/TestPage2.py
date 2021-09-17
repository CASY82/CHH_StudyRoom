#kakao internship
#프로그래밍 2번(스와이프) 실패!

rows = 4
columns = 3
swipes = [[1,1,2,4,3],[3,2,1,2,3],[4,1,1,4,3],[2,2,1,3,3]]


def solution(rows, columns, swipes):
    answer = []
    array_pro = [[0 for i in range(columns)] for j in range(rows)]
    d = 0
    num = 1

    for i in range(rows):
        for j in range(columns):
            array_pro[i][j] = num
            num += 1

    for i in range(4):
        d = swipes[i][0]
        r1 = swipes[i][1]-1
        c1 = swipes[i][2]-1
        r2 = swipes[i][3]-1
        c2 = swipes[i][4]-1

        for a in range(r1, r2):
            for b in range(c1, c2):
                if d == 1:
                    tmp = array_pro[a][b]
                    if a < (rows-1):
                        array_pro[a + 1][b] = array_pro[a][b]
                    else:
                        array_pro[r1][b] = tmp
                if d == 2:
                    tmp = array_pro[a][b]
                    if a > 0:
                        array_pro[a - 1][b] = array_pro[a][b]
                    else:
                        array_pro[r2][b] = tmp
                if d == 3:
                    tmp = array_pro[a][b]
                    if j < (columns-1):
                        array_pro[a][b + 1] = array_pro[a][b]
                    else:
                        array_pro[a][c1] = tmp
                if d == 4:
                    tmp = array_pro[a][b]
                    if j < (columns - 1):
                        array_pro[a][b - 1] = array_pro[a][b]
                    else:
                        array_pro[a][c2] = tmp

    print(array_pro)

    return answer

print(solution(rows, columns, swipes))