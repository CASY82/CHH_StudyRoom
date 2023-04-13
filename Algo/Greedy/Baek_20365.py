import sys

length = int(sys.stdin.readline())
quiz = sys.stdin.readline().strip()
result = 1

r_cnt = quiz.count("R")
b_cnt = quiz.count("B")

tmp_b = [x for x in quiz.split("B") if x != ""]
tmp_r = [x for x in quiz.split("R") if x != ""]

result += min(len(tmp_r), len(tmp_b))

print(result)

# 다른사람풀이

# import sys
#
# N = int(sys.stdin.readline())
# colors = sys.stdin.readline().rstrip()
# cnt_dict = {'R': 0, 'B': 0}
# state = ''
# for i in range(len(colors)):
#   if state != colors[i]:
#     state = colors[i]
#     cnt_dict[state] += 1
# #print(cnt_dict)
# print(min(cnt_dict.values()) + 1)