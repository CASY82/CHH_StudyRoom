import sys

s = sys.stdin.readline().strip()
q = int(sys.stdin.readline())

n = len(s)

prefix = [[0] * n for _ in range(26)]

prefix[ord(s[0]) - 97][0] = 1

for i in range(1, n):
    for j in range(26):
        prefix[j][i] = prefix[j][i - 1]
    prefix[ord(s[i]) - 97][i] += 1

for _ in range(q):
    alpha, l, r = input().split()
    l = int(l)
    r = int(r)
    idx = ord(alpha) - 97

    if l == 0:
        print(prefix[idx][r])
    else:
        print(prefix[idx][r] - prefix[idx][l - 1])