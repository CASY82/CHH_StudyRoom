import sys

n = int(sys.stdin.readline())

command = list(sys.stdin.readline().strip())
result = 0
skillLR_stack = []
skillSK_stack = []

for skill in range(len(command)):
    if command[skill] not in {'L', 'R', 'S', 'K'}:
        result += 1
    else:
        if command[skill] in {'S', 'K'}:
            if command[skill] == 'S':
                skillSK_stack.append(command[skill])
            else:
                try:
                    if skillSK_stack.pop() == 'S':
                        result += 1
                    else:
                        break
                except:
                    break
        else:
            if command[skill] == 'L':
                skillLR_stack.append(command[skill])
            else:
                try:
                    if skillLR_stack.pop() == 'L':
                        result += 1
                    else:
                        break
                except:
                    break

print(result)

# 다른 사람 풀이

# import sys
# input = sys.stdin.readline
#
# N = int(input())
# attack = input().rstrip()
#
# result = 0
# l_stk, s_stk = [], []
# for i in attack:
#     # 사전 기술
#     if i == 'L':
#         l_stk.append(i)
#     elif i == 'S':
#         s_stk.append(i)
#     # 본 기술
#     elif i == 'R':
#         if l_stk:
#             l_stk.pop()
#             result += 1
#         elif s_stk or not l_stk:
#             break
#     elif i == 'K':
#         if s_stk:
#             s_stk.pop()
#             result += 1
#         elif l_stk or not s_stk:
#             break
#     # 사전 기술 없이 사용 가능 기술
#     else:
#         result += 1
#
# print(result)

# 다른사람 풀이 2

# N=int(input())
# skills=list(input())
# pre_skills={"L":0, "S":0}
# # L -> R
# # S -> K
#
# success=0
# for s in skills:
#     if s.isnumeric():
#         success+=1
#     elif s=="L" or s=="S":
#         pre_skills[s]+=1
#     elif s=="R":
#         if pre_skills["L"]>=1:
#             success+=1
#             pre_skills["L"]-=1
#         else:
#             break
#     elif s=="K":
#         if pre_skills["S"]>=1:
#             success+=1
#             pre_skills["S"]-=1
#         else:
#             break
# print(success)