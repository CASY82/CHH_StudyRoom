while True:
    tree = list(map(int, input().split()))
    leaf = 1

    if tree[0] == 0:
        break

    for i in range(1, len(tree)):
        if i % 2 == 1:
            leaf *= tree[i]
        else:
            leaf -= tree[i]

    print(leaf)