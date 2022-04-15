import sys

while True:
    n = sys.stdin.readline().strip()
    k = 2

    if n == "":
        break

    num_cnt = [0 for _ in range(10)]

    for i in range(len(n)):
        num_cnt[int(n[i])] += 1

    tmp_n = int(n)

    while num_cnt.count(0) != 0:
        tmp = str(tmp_n * k)

        for i in range(len(tmp)):
            num_cnt[int(tmp[i])] += 1

        k += 1

    print(k-1)