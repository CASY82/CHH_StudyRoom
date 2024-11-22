import sys

n = int(sys.stdin.readline())

candidate = dict()

for _ in range(n):
    name = sys.stdin.readline().strip()
    if name not in candidate:
        candidate[name] = 1
    else:
        candidate[name] += 1

max_value = max(candidate.values())
max_keys = [key for key, value in candidate.items() if value == max_value]
max_keys.sort()

for key in max_keys:
    print(key)

# 다른 사람 풀이
# import sys
#
# input = lambda: sys.stdin.readline().strip()
#
# poll_dict = {}
#
# for _ in range(int(input())):
#     name = input()
#     poll_dict[name] = poll_dict.get(name, 0) + 1
#
# max_votes = max(poll_dict.values())
#
# tmp = []
#
# for name, votes in poll_dict.items():
#     if votes == max_votes:
#         tmp.append(name)
#
# tmp.sort()
#
# print(*tmp, sep="\n")