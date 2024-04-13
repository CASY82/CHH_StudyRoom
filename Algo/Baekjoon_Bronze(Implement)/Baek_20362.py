import sys

n, correcter = sys.stdin.readline().strip().split()

n = int(n)

candidate_answer = []
answer = ""
check = True

result = 0

for _ in range(n):
    nickname, ans = sys.stdin.readline().strip().split()

    if nickname == correcter:
        answer = ans
        check = False

    if check:
        candidate_answer.append(ans)

for ans in candidate_answer:
    if ans == answer:
        result += 1

print(result)

# 다른 사람 풀이
# n, s = input().split()
# ans = 0
# lst = []
# for i in range(int(n)):
#     x, y = input().split()
#     if x == s:
#         break
#     lst.append(y)
# print(lst.count(y))