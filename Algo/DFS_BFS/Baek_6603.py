import sys
sys.setrecursionlimit(10 ** 5)

def backtrack(x, start, numList, check, locate):
    if x == 6:
        for i in locate:
            print(i, end=' ')
        print()

    else:
        for i in range(start, len(numList)):
            if not check[i]:
                check[i] = True
                locate.append(numList[i])
                backtrack(x+1, i, numList, check, locate)
                locate.pop()
                check[i] = False

while True:
    num = list(map(int, sys.stdin.readline().split()))
    locate = []
    lotto = num[1:]
    check = [False] * len(lotto)

    if num[0] == 0:
        break

    backtrack(0, 0, lotto, check, locate)
    print()