#분명 정렬문제지만... 난 해시를 이용하여 풀기로했다...
import sys

n = int(sys.stdin.readline())
compareNum = set(list(map(int, sys.stdin.readline().split())))

m = int(sys.stdin.readline())
checkNum = list(map(int, sys.stdin.readline().split()))

result = [0] * m

for i in range(m):
    if checkNum[i] in compareNum:
        result[i] = 1

for i in result:
    print(i, end=' ')