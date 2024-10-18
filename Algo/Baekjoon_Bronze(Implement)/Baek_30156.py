import sys

t = int(sys.stdin.readline())

for _ in range(t):
    s = sys.stdin.readline().strip()

    a_cnt = s.count("a")
    b_cnt = s.count("b")

    print(min(a_cnt, b_cnt))