import sys

n, m = map(int, sys.stdin.readline().split())
s = sys.stdin.readline().strip()
res = True
res_s = ""
condition = 1

# 맨 뒷글자는 자음 제외
# 뒤에서 두,세번째는 A

if s.count("A") < 2:
    res = False
elif len(s) < m:
    res = False
else:
    revers_s = s[::-1]
    a_cnt = 0

    # 자음 제외
    for i in range(len(revers_s)):
        if revers_s[i] not in ["A", "E", "I", "O", "U"] and condition == 1:
            res_s += revers_s[i]
            condition += 1

        if condition == 2:
            if revers_s[i] == "A" and a_cnt < 2:
                res_s += "A"
                a_cnt += 1
            elif a_cnt == 2:
                condition += 1

        if condition == 3:
            res_s += revers_s[i:]
            break

    res_s = res_s[:m]
    res_s = res_s[::-1]

if condition != 3 or len(res_s) != m:
    res = False

if res:
    print("YES")
    print(res_s)
else:
    print("NO")

# 다른 사람 풀이
# from sys import stdin
# from collections import deque
#
# input = stdin.readline
#
# n, m = map(int, input().split())
# q = deque(input().rstrip())
# res = ''
#
# while q and q[-1] in 'AEIOU':
#     q.pop()
#
# if q:
#     res = q.pop()
#
# for _ in range(2):
#     while q and q[-1] != 'A':
#         q.pop()
#
#     if q:
#         res = q.pop() + res
#
# res = ''.join(q) + res
# print(['NO', 'YES\n' + res[-m:]][len(res) >= m])