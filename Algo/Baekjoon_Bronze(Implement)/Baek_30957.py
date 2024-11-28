import sys

n = int(sys.stdin.readline())
memo = sys.stdin.readline().strip()

b_cnt = memo.count("B")
a_cnt = memo.count("A")
s_cnt = memo.count("S")

max_cnt = max(a_cnt, b_cnt, s_cnt)
res = ""

if max_cnt == a_cnt == s_cnt == b_cnt:
    res = "SCU"
else:
    if max_cnt == b_cnt:
        res += "B"

    if max_cnt == s_cnt:
        res += "S"

    if max_cnt == a_cnt:
        res += "A"

print(res)