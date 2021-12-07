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

# 시간이 굉장히 짧아서 가져와본 코드
# import sys
#
#
# cache = {}
#
#
# def hanoi(num, s, t):
#     global cache
#     if num == 1:
#         return f'{s} {t}\n'
#     if (num, s, t) in cache:
#         return cache[(num, s, t)]
#     o = 6 - s - t
#     result = hanoi(num-1, s, o) + \
#         f'{s} {t}\n' + hanoi(num-1, o, t)
#     cache[(num, s, t)] = result
#     return result
#
#
# def solve():
#     N = int(sys.stdin.readline().rstrip())
#     print(2**N - 1)
#     print(hanoi(N, 1, 3))
#
#
# if __name__ == "__main__":
#     solve()
#
#     cache = {}

# 위 아래 두 풀이 모두 cache를 이용하였다... 정확히 어떤 기능을 하는지 알아봐야할 필요가 생겼다.
# def hanoi(front, middle, back, N):
#     if N == 1:
#         return f'{front} {back}\n'
#     if (front, middle, back, N) in cache:
#         return cache[(front, middle, back, N)]
#     else:
#         cur = [hanoi(front, back, middle, N - 1), f'{front} {back}\n', hanoi(middle, front, back, N - 1)]
#         cache[(front, middle, back, N)] = ''.join(cur)
#         return cache[(front, middle, back, N)]
#
#
# n = int(input())
# sum = 1
# for i in range(n - 1):
#     sum = sum * 2 + 1
# print(sum)
# print(hanoi(1, 2, 3, n))

#정석 풀이 코드 짧은 것

# def hanoi(n,start,end):
#     if n== 1:
#         print(start,end)
#         return
#     hanoi(n-1,start,6-start-end)
#     print(start,end)
#     hanoi(n-1,6-start-end,end)
#
# n = int(input())
# print(2**n-1)
# hanoi(n,1,3)