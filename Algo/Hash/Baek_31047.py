import sys
from collections import defaultdict

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())

    product = defaultdict(int)

    for _ in range(n):
        name, cnt = sys.stdin.readline().strip().split()
        cnt = int(cnt)
        product[name] += cnt


    tmp = list(product.items())
    tmp.sort(key=lambda x: (-x[1], x[0]))

    print(len(tmp))
    for i in range(len(tmp)):
        print(tmp[i][0], tmp[i][1])