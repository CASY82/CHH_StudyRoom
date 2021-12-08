import sys
sys.setrecursionlimit(10 ** 6)
k = int(sys.stdin.readline())

def hanoi(n, start, end, via):
    if n <= 1:
        print(start, end)

    else:
        hanoi(n-1, start, via, end)
        print(start, end)
        hanoi(n-1, via, end, start)

def hanoi_result(n):
    if n <= 1:
        return 1
    else:
        return 2 * hanoi_result(n-1) + 1

print(hanoi_result(k))
if k <= 20:
    hanoi(k, 1, 3, 2)
