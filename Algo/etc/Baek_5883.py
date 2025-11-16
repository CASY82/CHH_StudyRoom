import sys

n = int(sys.stdin.readline())
cap = [int(sys.stdin.readline()) for _ in range(n)]

tmp = set(cap)
ans = 0

for rm in tmp:
    prev = None
    curr_len = 0
    max_len = 0

    for v in cap:
        if v == rm:
            continue

        if prev is None or v != prev:
            prev = v
            curr_len = 1
        else:
            curr_len += 1

        max_len = max(curr_len, max_len)

    ans = max(ans, max_len)

print(ans)