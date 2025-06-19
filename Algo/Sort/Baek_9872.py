import sys

n = int(sys.stdin.readline())
names = dict()

for _ in range(n):
    name_sets = sys.stdin.readline().strip().split()

    name_sets.sort()
    tmp = tuple(name_sets)

    if tmp not in names:
        names[tmp] = 1
    else:
        names[tmp] += 1

max_key = max(names, key=lambda x: names[x])

print(names[max_key])