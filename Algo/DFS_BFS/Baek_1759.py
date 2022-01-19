# 여기서 최소 한 개의 모음(a, e, i, o, u)과 최소 두 개의 자음으로 구성 --> 이것만 하면됨
# 알파벳이 암호에서 증가하는 순서로 배열 --> sort로 해결
import sys
sys.setrecursionlimit(10**5)

l, c = map(int, sys.stdin.readline().split())
alpha = list(sys.stdin.readline().strip().split())
vowels = 'a,e,i,o,u'.split(',')

alpha.sort()

check = [True] * c
cypher = []

#백트래킹 기본 골자 완성
def backtrack(n, next):
    if n == l:
        cnt = 0
        #모음 갯수만 센다.
        for k in cypher:
            if k in vowels:
                cnt += 1

        if cnt >= 1 and len(cypher)-cnt >= 2:
            for i in cypher:
                print(i, end='')
            print()

    else:
        for i in range(next, c):
            if check[i]:
                check[i] = False
                cypher.append(alpha[i])
                backtrack(n+1, i)
                cypher.pop()
                check[i] = True

backtrack(0, 0)