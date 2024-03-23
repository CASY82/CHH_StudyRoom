import sys

n, m = map(int, sys.stdin.readline().split())

answer = 0

for _ in range(n):
    vote = list(sys.stdin.readline().strip())
    o_cnt = 0

    for result in vote:
        if result == "O":
            o_cnt += 1

    if o_cnt >= (m // 2) + 1:
        answer += 1

print(answer)