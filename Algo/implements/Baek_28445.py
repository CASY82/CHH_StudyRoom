import sys

daddy_body, daddy_tail = sys.stdin.readline().strip().split()
mommy_body, mommy_tail = sys.stdin.readline().strip().split()

result = []
tmp = set()

tmp.add(daddy_tail)
tmp.add(daddy_body)
tmp.add(mommy_body)
tmp.add(mommy_tail)

tmp_list = list(tmp)

for i in range(len(tmp_list)):
    for j in range(len(tmp_list)):
        combination = tmp_list[i] + " " + tmp_list[j]

        result.append(combination)

result.sort()

for color in result:
    print(color)

# 다른 사람 풀이
# import itertools
#
# color=input().split()
# color+=input().split()
# #print(color)
# color=sorted(list(set(color)))
# for child in itertools.product(color, repeat = 2):
#     print(child[0],child[1])