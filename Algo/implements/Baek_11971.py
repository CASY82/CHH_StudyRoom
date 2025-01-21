import sys

n, m = map(int, sys.stdin.readline().split())
rule = []
run = []
load = 0
res = 0

for _ in range(n):
    rule.append(list(map(int, sys.stdin.readline().split())))

for _ in range(m):
    run.append(list(map(int, sys.stdin.readline().split())))

now_rule = rule[0][0]
now_rule_speed = rule[0][1]
now_run = run[0][0]
now_run_speed = run[0][1]
rule_index = 1
run_index = 1

while load < 100:
    if now_rule <= load:
        now_rule += rule[rule_index][0]
        now_rule_speed = rule[rule_index][1]
        rule_index += 1

    if now_run <= load:
        now_run += run[run_index][0]
        now_run_speed = run[run_index][1]
        run_index += 1

    res = max(res, now_run_speed - now_rule_speed)

    load += 1

print(res)

# 다른 사람 풀이
# l = []
# v = []
# x = []
# n, m = map(int, input().split())
# for i in range(n):
#     a, b = map(int, input().split())
#     for j in range(a):
#         l.append(b)
# for i in range(m):
#     a, b = map(int, input().split())
#     for j in range(a):
#         v.append(b)
# for i in range(len(l)):
#     if l[i] < v[i]:
#         x.append(v[i]-l[i])
# if x == []:
#     print(0)
# else:
#     print(max(x))