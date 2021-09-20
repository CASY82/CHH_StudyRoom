n, m = map(int, input().split())
guitar_set = []
guitar_sol = []
result = 0

for _ in range(m):
    a, b = map(int, input().split())
    guitar_set.append(a)
    guitar_sol.append(b)

if n <= 6:
    if n * min(guitar_sol) <= min(guitar_set):
        result += n * min(guitar_sol)
    else:
        result += min(guitar_set)
else:
    while True:
        if min(guitar_set) < min(guitar_sol) * 6:
            n -= 6
            result += min(guitar_set)
        else:
            n -= 6
            result += min(guitar_sol) * 6

        if n <= 6:
            if n * min(guitar_sol) <= min(guitar_set):
                result += n * min(guitar_sol)
                n = 0
            else:
                result += min(guitar_set)
                n = 0

        if n == 0:
            break

print(result)

# 참고용 다른 사람 풀이 굳이 리스트 안써도 되네..
# import sys
#
# n, m = map(int, sys.stdin.readline().split())
# min_p, min_pi = 1000, 1000
#
# for i in range(m):
#     a, b = map(int, sys.stdin.readline().split())
#     min_p = min(min_p, a)
#     min_pi = min(min_pi, b)
#
# cnt = n // 6 + 1
# m_result = 100000000
#
# for i in range(cnt + 1):
#     result = 0
#     tmp = n
#     tmp -= i * 6
#     result += i * min_p
#     if tmp > 0:
#         result += tmp * min_pi
#     m_result = min(m_result, result)
#
# print(m_result)
