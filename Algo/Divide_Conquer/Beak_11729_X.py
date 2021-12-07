# 혼자 힘으로 풀지 못하였다. 하노이의 탑 알고리즘 관련하여 자료를 보고 점화식을 참고하여 풀었다.
import sys
n = int(sys.stdin.readline())

def move(N, start, to):
    print(start, to)

def hanoi(n, start, to, via):
    if n == 1:
        move(1, start, to)
    else:
        hanoi(n-1, start, via, to)
        move(n, start, to)
        hanoi(n - 1, via, to, start)

def hanoi_result(n):
    if n == 1:
        return 1
    else:
        return 2 * hanoi_result(n-1) + 1

print(hanoi_result(n))
hanoi(n, 1, 3, 2)