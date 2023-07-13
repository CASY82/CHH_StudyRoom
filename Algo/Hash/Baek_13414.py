import sys

k, l = map(int, sys.stdin.readline().split())

user_list = dict()
now = 1
que = []

for _ in range(l):
    school_id = sys.stdin.readline().strip()

    user_list[school_id] = now
    now += 1

sorted_dict = sorted(user_list.items(), key=lambda x: x[1])

for i in range(k):
    if i < len(sorted_dict):
        print(sorted_dict[i][0])