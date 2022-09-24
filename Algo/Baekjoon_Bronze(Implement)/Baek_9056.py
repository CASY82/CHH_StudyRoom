import sys

t = int(sys.stdin.readline())

for _ in range(t):
    word, compare = sys.stdin.readline().strip().split()
    result = True
    alp = []
    using_check = []

    for i in range(len(word)):
        alp.append(word[i])
        using_check.append(0)

    for check in range(len(compare)):
        if compare[check] in alp:
            using_check[alp.index(compare[check])] = 1
        else:
            result = False

    if result and sum(using_check) == len(word):
        print("YES")
    else:
        print("NO")