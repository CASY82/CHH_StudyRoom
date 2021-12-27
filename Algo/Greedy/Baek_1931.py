# 반례를 통과 못함... 애초에 조금 이상하게 답이 나오는 상태...
# 3
# 3 5
# 1 4
# 4 4

# import sys
#
# n = int(sys.stdin.readline())
# meetings = []
# result = []
#
# for _ in range(n):
#     meetings.append(list(map(int, sys.stdin.readline().split())))
#
# meetings.sort(key = lambda x : (x[0], x[1]-x[0]))
#
# print(meetings)
#
# for i in range(len(meetings)):
#     result.append(meetings[i])
#
#     if len(result) >= 2:
#         if result[-1][1] - result[-1][0] < result[-2][1] - result[-2][0] and result[-2][1] > result[-1][0]:
#             result.pop(-2)
#
# print("중간", result)
#
# for j in range(len(result)-1, 0, -1):
#     if result[j-1][1] > result[j][0]:
#         result.pop(j-1)
#
#         print(result)
#
# print(len(result))

#아... 정렬까지는 맞았는데 조건을 선택하는 방법에서 해메다가 결국 보고 풀게되었다... 답을 보고나니 내가 너무 어렵게 접근하고 있었다....
import sys

n = int(sys.stdin.readline())
meetings = []
result = 1

for _ in range(n):
    meetings.append(list(map(int, sys.stdin.readline().split())))

meetings.sort(key = lambda x : (x[1], x[0]))

#어차피 정렬이 되어있으니 최초를 잡고 endtime만 비교하면 되는 문제였다니;;
end_time = meetings[0][1]
for i in range(1, len(meetings)):
    if meetings[i][0] >= end_time:
        result += 1
        end_time = meetings[i][1]

print(result)