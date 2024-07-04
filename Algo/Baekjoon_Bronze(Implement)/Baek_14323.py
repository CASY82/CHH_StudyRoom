import sys

t = int(sys.stdin.readline())

for i in range(1, t + 1):
    n = int(sys.stdin.readline())
    all_set = []

    for _ in range(n):
        name = sys.stdin.readline().strip()
        name_set = set()

        for j in range(len(name)):
            if name[j] == " ":
                continue
            name_set.add(name[j])

        all_set.append(("".join(name), len(name_set)))

    all_set.sort(key=lambda x:(-x[1], x[0]))

    print("Case #{0}: {1}".format(i, all_set[0][0]))