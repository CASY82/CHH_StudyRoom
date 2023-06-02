import sys

trees = dict()
result = []
total = 0

while True:
    tree = sys.stdin.readline().strip()

    if tree == "":
        break

    if tree not in trees:
        trees[tree] = 1
    else:
        trees[tree] += 1

total = sum(trees.values())

for key, val in trees.items():
    percent_tree = "%.4f" % ((val/total)*100)
    result.append((key, percent_tree))

result.sort(key = lambda x : x[0])

for trname, percent in result:
    print(trname, percent)