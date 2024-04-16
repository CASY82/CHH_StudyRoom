import sys

n = int(sys.stdin.readline())
homework = []
result = 0

for _ in range(n):
    command = list(sys.stdin.readline().strip().split())

    if command[0] == "0":
        if len(homework) > 0:
            if homework[-1][1] > 0:
                homework[-1][1] -= 1
                if homework[-1][1] == 0:
                    score, time = homework.pop()
                    result += score
    else:
        doing = [int(command[1]), int(command[2]) - 1]

        if doing[1] == 0:
            result += doing[0]
            continue

        homework.append(doing)

print(result)

# 다른 사람 풀이
# a=[]
# def push(n):
#     a.append(n)
# def pop():
#     if len(a)==0:
#         return 0
#     else:
#         n=a.pop()
#         return n
# x=0
# b=int(input())
# for i in range(b):
#     p=list(map(int, input().split()))
#     if p[0]==0:
#         m=pop()
#         if m!=0:
#             if m[1]==1:
#                 x+=m[0]
#             else:
#                 m[1]-=1
#                 push(m)
#     else:
#         if p[2]==1:
#             x+=p[1]
#         else:
#             push([p[1],p[2]-1])
# print(x)

# 다른 사람 풀이 2

# import sys
# input = sys.stdin.readline
#
# T = int(input())
#
# stack = []
# re_val = 0
#
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for test_case in range(1, T + 1):
#     tmp = input().split('\n')
#     tmp = tmp[0]
#
#     if tmp == '0':
#         # 이전 과제를 한다
#         if stack:
#             max_s, cal_time = stack.pop()
#             if cal_time == 1:
#                 re_val += max_s
#             else:
#                 stack.append([max_s, cal_time-1])
#
#         continue
#
#     hw_flag, max_score, during = tmp.split(' ')
#
#     max_score = int(max_score)
#     during = int(during)
#
#     # 과제 받자마자 바로 수행함.
#     if during == 1:
#         re_val += max_score
#         continue
#
#     # 0 이면 이전 과제 이어서 한다.
#     # 1 이면 새로운 과제를 한다.
#     # 새로운 과제가 끝나면 이전 과제를 한다.
#
#     stack.append([max_score, during-1])
#
# print(re_val)