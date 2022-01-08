import sys

bingo = []
check = []

for _ in range(5):
    bingo.append(list(map(int, sys.stdin.readline().split())))

for _ in range(5):
    check += list(map(int, sys.stdin.readline().split()))

def checker(bingo):
    cnt = 0
    #행 check
    for i in range(len(bingo)):
        if sum(bingo[i]) == 0:
            cnt += 1

    #열 check
    for i in range(len(bingo)):
        tmp = 0
        for j in range(len(bingo)):
            tmp += bingo[j][i]

        if tmp == 0:
            cnt += 1

    #대각 check
    tmp = 0
    for i in range(len(bingo)):
        tmp += bingo[i][i]

    if tmp == 0:
        cnt += 1

    #역 대각 check
    tmp = 0
    for i in range(len(bingo)):
        tmp += bingo[len(bingo)- 1 - i][i]

    if tmp == 0:
        cnt += 1

    return cnt

num = 0
while checker(bingo) < 3:
    for i in range(len(bingo)):
        looper = False
        for j in range(len(bingo)):
            if bingo[i][j] == check[num]:
                num += 1
                bingo[i][j] = 0
                looper = True
                break
        if looper:
            break
print(num)