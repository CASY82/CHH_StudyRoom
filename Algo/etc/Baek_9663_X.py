#로직은 다들 이것으로 하나 파이썬으로는 제한 시간 복잡도 내에서 성공하지 못하는 문제 pypy로 일단 통과하였다.
import sys

n = int(sys.stdin.readline())

chess = [0 for _ in range(n)] #index가 행값 value가 열값
locate = [False for _ in range(n)]

result = 0

def ChessBacktrack(x):
    if x == n:
        global result

        result += 1

    else:
        for i in range(n):
            if locate[i]:
                continue

            chess[x] = i

            if check(x):
                locate[i] = True
                ChessBacktrack(x + 1)
                locate[i] = False

def check(x):
    for j in range(x):
        if chess[x] == chess[j] or (abs(chess[x] - chess[j]) == (x - j)):
            return False

    return True

ChessBacktrack(0)
print(result)

#대부분 파이썬 풀이는 그냥 답을 때려넣는 형식으로 풀고있다... 이게 맞나?
# print([0,1,0,0,2,10,4,40,92,352,724,2680,14200,73712,365596][int(input())])