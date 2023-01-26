import sys

n, k = map(int, sys.stdin.readline().split())

def backtrack(sum_num, result):
    global cnt
    if sum_num > n:
        return
    if n == sum_num:
        cnt += 1
        if cnt == k:
            #마지막 + 빼는 부분
            print(result[:-1])
            exit()

    #1, 2, 3을 더한 결과들을 전부 순회한다.
    for i in (1, 2, 3):
        # 문자열로 바로 더하는게 빠르네...
        backtrack(sum_num + i, result+str(i)+"+")

cnt = 0
backtrack(0, '')
print(-1)